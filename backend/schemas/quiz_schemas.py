"""
Quiz Schemas - DTOs for quiz operations
Data transfer objects for quiz cards, answers, and submissions
"""

from dataclasses import dataclass
from typing import List, Optional

from backend.database.models import QuizCard, QuizAnswer, UserCard


@dataclass
class QuizAnswerResponse:
    """Response schema for quiz answer option."""
    id: int
    answer_text: str
    is_correct: bool
    explanation: Optional[str] = None

    @classmethod
    def from_model(cls, answer: QuizAnswer) -> 'QuizAnswerResponse':
        """
        Create QuizAnswerResponse from QuizAnswer model.
        
        Args:
            answer: QuizAnswer model instance
            
        Returns:
            QuizAnswerResponse instance
        """
        return cls(
            id=answer.answer_id,
            answer_text=answer.answer_text,
            is_correct=answer.is_correct,
            explanation=answer.explanation
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'answer_text': self.answer_text,
            'is_correct': self.is_correct,
            'explanation': self.explanation,
        }


@dataclass
class QuizCardResponse:
    """Response schema for quiz card with answers."""
    id: int
    concept_id: int
    question: str
    answers: List[QuizAnswerResponse]

    @classmethod
    def from_model(cls, quiz_card: QuizCard) -> 'QuizCardResponse':
        """
        Create QuizCardResponse from QuizCard model.
        
        Args:
            quiz_card: QuizCard model instance with answers loaded
            
        Returns:
            QuizCardResponse instance
        """
        answers = [
            QuizAnswerResponse.from_model(answer)
            for answer in quiz_card.answers
        ]
        
        return cls(
            id=quiz_card.quiz_card_id,
            concept_id=quiz_card.concept_id,
            question=quiz_card.question,
            answers=answers
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'concept_id': self.concept_id,
            'question': self.question,
            'answers': [answer.to_dict() for answer in self.answers],
        }


@dataclass
class QuizSubmitRequest:
    """Request schema for quiz answer submission."""
    quiz_card_id: int
    selected_answer_id: int
    is_correct: bool


@dataclass
class QuizSubmitResponse:
    """Response schema for quiz submission result."""
    quiz_card_id: int
    is_correct: bool
    success_count: int
    failure_count: int
    ease_factor: float
    next_review_days: int

    @classmethod
    def from_user_card(cls, user_card: UserCard) -> 'QuizSubmitResponse':
        """
        Create QuizSubmitResponse from UserCard model.
        
        Args:
            user_card: UserCard model instance
            
        Returns:
            QuizSubmitResponse instance
        """
        # Determine if the last answer was correct
        # by checking if success_count increased
        is_correct = (
            user_card.repetitions > 0
            if hasattr(user_card, 'repetitions')
            else True
        )
        
        return cls(
            quiz_card_id=user_card.quiz_card_id,
            is_correct=is_correct,
            success_count=user_card.success_count,
            failure_count=user_card.failure_count,
            ease_factor=user_card.ease_factor,
            next_review_days=user_card.interval_days
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'quiz_card_id': self.quiz_card_id,
            'is_correct': self.is_correct,
            'success_count': self.success_count,
            'failure_count': self.failure_count,
            'ease_factor': self.ease_factor,
            'next_review_days': self.next_review_days,
        }
