"""
Concept Service Module.

This module provides business logic for concept-related operations,
including concept retrieval and concept quiz cards.

Classes:
    ConceptService: Service for managing concept operations
"""

from typing import Optional, List, Dict, Any

from backend.database.models import Concept, QuizCard, QuizAnswer
from backend.services.base_service import BaseService


class ConceptService(BaseService):
    """
    Service for concept management operations.
    
    This service handles:
    - Concept retrieval
    - Concept quiz cards retrieval with answers
    - Concept and quiz card data serialization
    
    Inherits from BaseService for common database operations.
    
    Example:
        concept_service = ConceptService(db_session=db)
        concept = concept_service.get_concept_by_id(1)
    """
    
    def get_concept_by_id(self, concept_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific concept by ID.
        
        Args:
            concept_id: The unique identifier of the concept
        
        Returns:
            Concept dictionary or None if not found:
            {
                'id': int,
                'unit_id': int,
                'name': str,
                'tag': str,
                'definition': str
            }
            
        Example:
            concept = concept_service.get_concept_by_id(1)
            if concept:
                print(f"Concept: {concept['name']}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        concept = self.db_session.query(Concept).filter(
            Concept.concept_id == concept_id
        ).first()
        
        if not concept:
            return None
        
        return self.serialize_concept(concept)
    
    def get_concept_quiz_cards(
        self,
        concept_id: int
    ) -> List[Dict[str, Any]]:
        """
        Retrieve all quiz cards for a specific concept with answers.
        
        Each quiz card includes all its associated answers with
        correctness flags and explanations.
        
        Args:
            concept_id: The unique identifier of the concept
        
        Returns:
            List of quiz card dictionaries with structure:
            [{
                'id': int,
                'concept_id': int,
                'question': str,
                'answers': [{
                    'id': int,
                    'answer_text': str,
                    'is_correct': bool,
                    'explanation': str
                }, ...]
            }, ...]
            
        Example:
            cards = concept_service.get_concept_quiz_cards(1)
            for card in cards:
                print(f"Q: {card['question']}")
                for ans in card['answers']:
                    mark = '✓' if ans['is_correct'] else '✗'
                    print(f"  {mark} {ans['answer_text']}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        # Query all quiz cards for this concept
        quiz_cards = self.db_session.query(QuizCard).filter(
            QuizCard.concept_id == concept_id
        ).all()
        
        # For each quiz card, fetch its answers and serialize
        result = []
        for card in quiz_cards:
            answers = self.db_session.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == card.quiz_card_id
            ).all()
            
            result.append(
                self.serialize_quiz_card_with_answers(card, answers)
            )
        
        return result
    
    @staticmethod
    def serialize_concept(concept: Concept) -> Dict[str, Any]:
        """
        Convert a Concept model instance to a dictionary.
        
        Args:
            concept: The Concept model instance to serialize
        
        Returns:
            Dictionary with concept data:
            {
                'id': int,
                'unit_id': int,
                'name': str,
                'tag': str,
                'definition': str
            }
            
        Note:
            Currently 'tag' uses the title field as a placeholder.
        """
        return {
            'id': concept.concept_id,
            'unit_id': concept.unit_id,
            'name': concept.title,
            # TODO: Update when tag field is added to Concept model
            'tag': concept.title,
            'definition': concept.definition
        }
    
    @staticmethod
    def serialize_quiz_card_with_answers(
        quiz_card: QuizCard,
        answers: List[QuizAnswer]
    ) -> Dict[str, Any]:
        """
        Convert a QuizCard with its answers to a dictionary.
        
        Args:
            quiz_card: The QuizCard model instance
            answers: List of QuizAnswer model instances for this card
        
        Returns:
            Dictionary with quiz card and answers:
            {
                'id': int,
                'concept_id': int,
                'question': str,
                'answers': [
                    {
                        'id': int,
                        'answer_text': str,
                        'is_correct': bool,
                        'explanation': str
                    }, ...
                ]
            }
        """
        return {
            'id': quiz_card.quiz_card_id,
            'concept_id': quiz_card.concept_id,
            'question': quiz_card.question,
            'answers': [
                {
                    'id': ans.answer_id,
                    'answer_text': ans.answer_text,
                    'is_correct': ans.is_correct,
                    'explanation': ans.explanation
                }
                for ans in answers
            ]
        }
