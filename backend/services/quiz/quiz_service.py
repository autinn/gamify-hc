"""
Quiz Service Module.

This module provides business logic for quiz-related operations,
including quiz card retrieval, answer submission, and progress tracking.

Classes:
    QuizService: Service for managing quiz operations
"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from sqlalchemy.exc import IntegrityError

from backend.database.models import (
    QuizCard, QuizAnswer, UserCard, Concept, Unit
)
from backend.services.base_service import BaseService
from backend.services.serializers import serialize_quiz_card_with_answers


class QuizService(BaseService):
    """
    Service for quiz management operations.
    
    This service handles:
    - Quiz card retrieval (single and by course/unit)
    - Random quiz card selection
    - Answer submission and validation
    - User progress tracking (UserCard management)
    - Quiz data serialization
    
    Inherits from BaseService for common database operations.
    
    Example:
        quiz_service = QuizService(db_session=db)
        card = quiz_service.get_quiz_card_by_id(1)
    """
    
    def get_quiz_card_by_id(
        self,
        quiz_card_id: int
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific quiz card by ID with all its answers.
        
        Args:
            quiz_card_id: The unique identifier of the quiz card
        
        Returns:
            Quiz card dictionary or None if not found:
            {
                'id': int,
                'concept_id': int,
                'question': str,
                'answers': [{
                    'id': int,
                    'answer_text': str,
                    'is_correct': bool,
                    'explanation': str
                }, ...]
            }
            
        Example:
            card = quiz_service.get_quiz_card_by_id(1)
            if card:
                print(f"Q: {card['question']}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        quiz_card = self.db_session.query(QuizCard).filter(
            QuizCard.quiz_card_id == quiz_card_id
        ).first()
        
        if not quiz_card:
            return None
        
        answers = self.db_session.query(QuizAnswer).filter(
            QuizAnswer.quiz_card_id == quiz_card_id
        ).all()

        return serialize_quiz_card_with_answers(quiz_card, answers)
    
    def get_course_quiz_cards(self, course_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve all quiz cards for a specific course.
        
        Traverses the hierarchy: course -> units -> concepts -> quiz cards
        
        Args:
            course_id: The unique identifier of the course
        
        Returns:
            List of quiz card dictionaries with answers
            
        Example:
            cards = quiz_service.get_course_quiz_cards(1)
            print(f"Found {len(cards)} quiz cards")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        # Get all units for this course
        units = self.db_session.query(Unit).filter(
            Unit.course_id == course_id
        ).all()
        unit_ids = [u.unit_id for u in units]
        
        if not unit_ids:
            return []
        
        # Get all concepts for these units
        concepts = self.db_session.query(Concept).filter(
            Concept.unit_id.in_(unit_ids)
        ).all()
        concept_ids = [c.concept_id for c in concepts]
        
        # Get all quiz cards for these concepts
        return self._get_quiz_cards_for_concepts(concept_ids)
    
    def get_unit_quiz_cards(self, unit_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve all quiz cards for a specific unit.
        
        Traverses the hierarchy: unit -> concepts -> quiz cards
        
        Args:
            unit_id: The unique identifier of the unit
        
        Returns:
            List of quiz card dictionaries with answers
            
        Example:
            cards = quiz_service.get_unit_quiz_cards(1)
            print(f"Found {len(cards)} quiz cards")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        # Get all concepts for this unit
        concepts = self.db_session.query(Concept).filter(
            Concept.unit_id == unit_id
        ).all()
        concept_ids = [c.concept_id for c in concepts]
        
        # Get all quiz cards for these concepts
        return self._get_quiz_cards_for_concepts(concept_ids)
    
    def get_all_quiz_cards(self) -> List[Dict[str, Any]]:
        """
        Retrieve all quiz cards from the entire system.
        
        Used for random quiz mode where users want questions from
        all courses. Frontend will shuffle and limit these.
        
        Returns:
            List of all quiz card dictionaries with answers
            
        Example:
            cards = quiz_service.get_all_quiz_cards()
            print(f"Total quiz cards: {len(cards)}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        quiz_cards = self.db_session.query(QuizCard).all()

        result = []
        for qc in quiz_cards:
            answers = self.db_session.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == qc.quiz_card_id
            ).all()
            result.append(
                serialize_quiz_card_with_answers(qc, answers)
            )

        return result

    def submit_answer(
        self,
        user_id: int,
        quiz_card_id: int,
        answer_id: int,
        is_first_attempt: bool = True
    ) -> Dict[str, Any]:
        """
        Submit a quiz answer and update user progress.
        
        Validates the answer, checks correctness, and updates or creates
        the user's progress record (UserCard). Handles both new
        submissions and updates to existing progress.
        
        Args:
            user_id: The user's unique identifier
            quiz_card_id: The quiz card being answered
            answer_id: The selected answer
            is_first_attempt: Whether this is the first try (default True)
        
        Returns:
            Dictionary with submission result:
            {
                'is_correct': bool,
                'explanation': str,
                'times_seen': int,
                'times_correct': int
            }
            
        Raises:
            ValueError: If answer_id is invalid
            Exception: If database error occurs
            
        Example:
            result = quiz_service.submit_answer(
                user_id=1,
                quiz_card_id=1,
                answer_id=2,
                is_first_attempt=True
            )
            if result['is_correct']:
                print("Correct! " + result['explanation'])
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        # Validate that the answer exists
        answer = self.db_session.query(QuizAnswer).filter(
            QuizAnswer.answer_id == answer_id
        ).first()
        
        if not answer:
            raise ValueError('Invalid answer_id')
        
        is_correct = answer.is_correct
        
        try:
            # Find or create UserCard to track progress
            user_card = self.db_session.query(UserCard).filter(
                UserCard.user_id == user_id,
                UserCard.quiz_card_id == quiz_card_id
            ).first()
            
            if user_card:
                # Update existing progress record
                user_card.repetitions = (user_card.repetitions or 0) + 1
                if is_correct and is_first_attempt:
                    user_card.success_count = (
                        user_card.success_count or 0
                    ) + 1
                elif not is_correct:
                    user_card.failure_count = (
                        user_card.failure_count or 0
                    ) + 1
                user_card.last_reviewed = datetime.utcnow()
            else:
                # Create new progress record
                user_card = UserCard(
                    user_id=user_id,
                    quiz_card_id=quiz_card_id,
                    repetitions=1,
                    success_count=(
                        1 if (is_correct and is_first_attempt) else 0
                    ),
                    failure_count=0 if is_correct else 1,
                    last_reviewed=datetime.utcnow()
                )
                self.db_session.add(user_card)
            
            self.commit()
            self.refresh(user_card)
            
            return {
                'is_correct': is_correct,
                'explanation': answer.explanation,
                'times_seen': user_card.repetitions or 0,
                'times_correct': user_card.success_count
            }
            
        except IntegrityError:
            # Race condition: UserCard was created between check and insert
            self.rollback()
            
            # Retry with update
            user_card = self.db_session.query(UserCard).filter(
                UserCard.user_id == user_id,
                UserCard.quiz_card_id == quiz_card_id
            ).first()
            
            if not user_card:
                raise Exception('Failed to update progress')
            
            # Update existing progress record
            user_card.repetitions = (user_card.repetitions or 0) + 1
            if is_correct and is_first_attempt:
                user_card.success_count = (
                    user_card.success_count or 0
                ) + 1
            elif not is_correct:
                user_card.failure_count = (
                    user_card.failure_count or 0
                ) + 1
            user_card.last_reviewed = datetime.utcnow()
            
            self.commit()
            self.refresh(user_card)
            
            return {
                'is_correct': is_correct,
                'explanation': answer.explanation,
                'times_seen': user_card.repetitions or 0,
                'times_correct': user_card.success_count
            }
    
    def _get_quiz_cards_for_concepts(
        self,
        concept_ids: List[int]
    ) -> List[Dict[str, Any]]:
        """
        Internal helper to retrieve quiz cards for multiple concepts.
        
        Args:
            concept_ids: List of concept IDs to fetch quiz cards for
        
        Returns:
            List of quiz card dictionaries with answers
        """
        if not concept_ids:
            return []
        
        quiz_cards = self.db_session.query(QuizCard).filter(
            QuizCard.concept_id.in_(concept_ids)
        ).all()

        result = []
        for qc in quiz_cards:
            answers = self.db_session.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == qc.quiz_card_id
            ).all()
            result.append(
                serialize_quiz_card_with_answers(qc, answers)
            )

        return result
