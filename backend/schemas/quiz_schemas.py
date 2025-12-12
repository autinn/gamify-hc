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
    is_correct: bool
    times_seen: int
    times_correct: int
    explanation: Optional[str] = None

    @classmethod
    def from_model_with_explanation(
        cls,
        user_card: UserCard,
        is_correct: bool,
        explanation: Optional[str] = None
    ) -> 'QuizSubmitResponse':
        """
        Create QuizSubmitResponse from UserCard model.
        
        Args:
            user_card: UserCard model instance
            is_correct: Whether the answer was correct
            explanation: Explanation for the answer
            
        Returns:
            QuizSubmitResponse instance
        """
        # times_seen = total attempts (tracks all including retries)
        times_seen = user_card.repetitions
        
        return cls(
            is_correct=is_correct,
            times_seen=times_seen,
            times_correct=user_card.success_count,
            explanation=explanation
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'is_correct': self.is_correct,
            'times_seen': self.times_seen,
            'times_correct': self.times_correct,
            'explanation': self.explanation,
        }
