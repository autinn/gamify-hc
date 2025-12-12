"""
Quiz Repository - Quiz card and answer data access
Handles all database operations related to quiz cards and answers
"""

from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from backend.database.models import QuizCard, QuizAnswer
from backend.repositories.base_repository import BaseRepository


class QuizRepository(BaseRepository[QuizCard]):
    """
    Repository for QuizCard and QuizAnswer model operations.
    
    Provides methods for querying quiz cards and their answers,
    including filtering by course, unit, or concept.
    
    Example:
        >>> from backend.utils.database_manager import get_db
        >>> session = get_db()
        >>> quiz_repo = QuizRepository(session)
        >>> cards = quiz_repo.get_quiz_cards_by_course(1)
    """

    def __init__(self, session: Session):
        """
        Initialize quiz repository.
        
        Args:
            session: Database session
        """
        super().__init__(QuizCard, session)

    def get_quiz_card_by_id(self, quiz_card_id: int) -> Optional[QuizCard]:
        """
        Get a quiz card by its ID.
        
        Args:
            quiz_card_id: Quiz card unique identifier
            
        Returns:
            QuizCard instance or None if not found
            
        Example:
            >>> card = quiz_repo.get_quiz_card_by_id(42)
        """
        return self.get_by_id(quiz_card_id)

    def get_quiz_card_with_answers(
        self,
        quiz_card_id: int
    ) -> Optional[QuizCard]:
        """
        Get a quiz card with all its answers loaded.
        
        Uses eager loading for better performance.
        
        Args:
            quiz_card_id: Quiz card unique identifier
            
        Returns:
            QuizCard instance with answers loaded, or None if not found
            
        Example:
            >>> card = quiz_repo.get_quiz_card_with_answers(42)
            >>> for answer in card.answers:
            >>>     print(answer.answer_text)
        """
        return (
            self.session.query(QuizCard)
            .options(joinedload(QuizCard.answers))
            .filter(QuizCard.quiz_card_id == quiz_card_id)
            .first()
        )

    def get_answers_by_quiz_card(
        self,
        quiz_card_id: int
    ) -> List[QuizAnswer]:
        """
        Get all answers for a specific quiz card.
        
        Args:
            quiz_card_id: Quiz card unique identifier
            
        Returns:
            List of QuizAnswer instances
            
        Example:
            >>> answers = quiz_repo.get_answers_by_quiz_card(42)
        """
        return (
            self.session.query(QuizAnswer)
            .filter(QuizAnswer.quiz_card_id == quiz_card_id)
            .all()
        )

    def get_answer_by_id(self, answer_id: int) -> Optional[QuizAnswer]:
        """
        Get an answer by its ID.
        
        Args:
            answer_id: Answer unique identifier
            
        Returns:
            QuizAnswer instance or None if not found
            
        Example:
            >>> answer = quiz_repo.get_answer_by_id(105)
        """
        return (
            self.session.query(QuizAnswer)
            .filter(QuizAnswer.answer_id == answer_id)
            .first()
        )

    def get_quiz_cards_by_course(self, course_id: int) -> List[QuizCard]:
        """
        Get all quiz cards for a specific course.
        
        Uses denormalized course_id field for performance.
        
        Args:
            course_id: Course unique identifier
            
        Returns:
            List of QuizCard instances
            
        Example:
            >>> cards = quiz_repo.get_quiz_cards_by_course(1)
        """
        return (
            self.session.query(QuizCard)
            .filter(QuizCard.course_id == course_id)
            .all()
        )

    def get_quiz_cards_by_unit(self, unit_id: int) -> List[QuizCard]:
        """
        Get all quiz cards for a specific unit.
        
        Uses denormalized unit_id field for performance.
        
        Args:
            unit_id: Unit unique identifier
            
        Returns:
            List of QuizCard instances
            
        Example:
            >>> cards = quiz_repo.get_quiz_cards_by_unit(5)
        """
        return (
            self.session.query(QuizCard)
            .filter(QuizCard.unit_id == unit_id)
            .all()
        )

    def get_quiz_cards_by_concept(
        self,
        concept_id: int
    ) -> List[QuizCard]:
        """
        Get all quiz cards for a specific concept.
        
        Args:
            concept_id: Concept unique identifier
            
        Returns:
            List of QuizCard instances
            
        Example:
            >>> cards = quiz_repo.get_quiz_cards_by_concept(10)
        """
        return (
            self.session.query(QuizCard)
            .filter(QuizCard.concept_id == concept_id)
            .all()
        )

    def get_quiz_cards_by_concept_ids(
        self,
        concept_ids: List[int]
    ) -> List[QuizCard]:
        """
        Get all quiz cards for multiple concepts.
        
        Args:
            concept_ids: List of concept identifiers
            
        Returns:
            List of QuizCard instances
            
        Example:
            >>> cards = quiz_repo.get_quiz_cards_by_concept_ids([10, 11, 12])
        """
        if not concept_ids:
            return []
        
        return (
            self.session.query(QuizCard)
            .filter(QuizCard.concept_id.in_(concept_ids))
            .all()
        )

    def get_all_quiz_cards(self) -> List[QuizCard]:
        """
        Get all quiz cards in the system.
        
        Returns:
            List of all QuizCard instances
            
        Example:
            >>> all_cards = quiz_repo.get_all_quiz_cards()
        """
        return self.get_all()

    def get_random_quiz_cards(self, limit: int = 10) -> List[QuizCard]:
        """
        Get random quiz cards.
        
        Args:
            limit: Maximum number of cards to return
            
        Returns:
            List of random QuizCard instances
            
        Example:
            >>> random_cards = quiz_repo.get_random_quiz_cards(20)
        """
        from sqlalchemy import func
        
        return (
            self.session.query(QuizCard)
            .order_by(func.random())
            .limit(limit)
            .all()
        )

    def get_quiz_card_count_by_course(self, course_id: int) -> int:
        """
        Count quiz cards for a course.
        
        Args:
            course_id: Course unique identifier
            
        Returns:
            Number of quiz cards
            
        Example:
            >>> count = quiz_repo.get_quiz_card_count_by_course(1)
        """
        return (
            self.session.query(QuizCard)
            .filter(QuizCard.course_id == course_id)
            .count()
        )

    def get_quiz_card_count_by_unit(self, unit_id: int) -> int:
        """
        Count quiz cards for a unit.
        
        Args:
            unit_id: Unit unique identifier
            
        Returns:
            Number of quiz cards
            
        Example:
            >>> count = quiz_repo.get_quiz_card_count_by_unit(5)
        """
        return (
            self.session.query(QuizCard)
            .filter(QuizCard.unit_id == unit_id)
            .count()
        )

    def get_quiz_card_count_by_concept(self, concept_id: int) -> int:
        """
        Count quiz cards for a concept.
        
        Args:
            concept_id: Concept unique identifier
            
        Returns:
            Number of quiz cards
            
        Example:
            >>> count = quiz_repo.get_quiz_card_count_by_concept(10)
        """
        return (
            self.session.query(QuizCard)
            .filter(QuizCard.concept_id == concept_id)
            .count()
        )
