"""
User Schemas - DTOs for user progress operations
Data transfer objects for user progress and statistics
"""

from dataclasses import dataclass
from typing import Optional

from backend.database.models import UserCard


@dataclass
class UserProgressResponse:
    """Response schema for individual quiz card progress."""
    quiz_card_id: int
    times_seen: int
    times_correct: int
    last_seen: Optional[str] = None

    @classmethod
    def from_user_card(cls, user_card: UserCard) -> 'UserProgressResponse':
        """
        Create UserProgressResponse from UserCard model.
        
        Args:
            user_card: UserCard model instance
            
        Returns:
            UserProgressResponse instance
        """
        # Use repetitions for times_seen (tracks all attempts + retries)
        times_seen = user_card.repetitions
        
        return cls(
            quiz_card_id=user_card.quiz_card_id,
            times_seen=times_seen,
            times_correct=user_card.success_count,
            last_seen=(
                user_card.last_reviewed.isoformat()
                if user_card.last_reviewed else None
            )
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'quiz_card_id': self.quiz_card_id,
            'times_seen': self.times_seen,
            'times_correct': self.times_correct,
            'last_seen': self.last_seen,
        }


@dataclass
class ProgressStatsResponse:
    """Response schema for aggregated progress statistics."""
    total_cards: int
    cards_seen: int
    cards_not_seen: int
    total_attempts: int
    success_count: int
    failure_count: int
    success_rate: float
    completion_rate: float

    @classmethod
    def from_dict(cls, stats: dict) -> 'ProgressStatsResponse':
        """
        Create ProgressStatsResponse from statistics dictionary.
        
        Args:
            stats: Statistics dictionary from service layer
            
        Returns:
            ProgressStatsResponse instance
        """
        return cls(
            total_cards=stats.get('total_cards', 0),
            cards_seen=stats.get('cards_seen', 0),
            cards_not_seen=stats.get('cards_not_seen', 0),
            total_attempts=stats.get('total_attempts', 0),
            success_count=stats.get('success_count', 0),
            failure_count=stats.get('failure_count', 0),
            success_rate=stats.get('success_rate', 0.0),
            completion_rate=stats.get('completion_rate', 0.0),
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'total_cards': self.total_cards,
            'cards_seen': self.cards_seen,
            'cards_not_seen': self.cards_not_seen,
            'total_attempts': self.total_attempts,
            'success_count': self.success_count,
            'failure_count': self.failure_count,
            'success_rate': self.success_rate,
            'completion_rate': self.completion_rate,
        }
