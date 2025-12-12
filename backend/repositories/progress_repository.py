"""
Progress Repository - User progress and UserCard data access
Handles all database operations related to user progress tracking
"""

from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.database.models import UserCard, QuizCard
from backend.repositories.base_repository import BaseRepository


class ProgressRepository(BaseRepository[UserCard]):
    """
    Repository for UserCard (progress tracking) model operations.
    
    Provides methods for managing user progress on quiz cards,
    including spaced repetition data and success/failure tracking.
    
    Example:
        >>> from backend.utils.database_manager import get_db
        >>> session = get_db()
        >>> progress_repo = ProgressRepository(session)
        >>> progress = progress_repo.get_user_card(user_id=42, quiz_card_id=10)
    """

    def __init__(self, session: Session):
        """
        Initialize progress repository.
        
        Args:
            session: Database session
        """
        super().__init__(UserCard, session)

    def get_user_card(
        self,
        user_id: int,
        quiz_card_id: int
    ) -> Optional[UserCard]:
        """
        Get a specific UserCard by composite key.
        
        Args:
            user_id: User unique identifier
            quiz_card_id: Quiz card unique identifier
            
        Returns:
            UserCard instance or None if not found
            
        Example:
            >>> card = progress_repo.get_user_card(42, 10)
        """
        return (
            self.session.query(UserCard)
            .filter(
                UserCard.user_id == user_id,
                UserCard.quiz_card_id == quiz_card_id
            )
            .first()
        )

    def create_or_update_user_card(
        self,
        user_id: int,
        quiz_card_id: int,
        **data
    ) -> UserCard:
        """
        Create a new UserCard or update existing one.
        
        Args:
            user_id: User unique identifier
            quiz_card_id: Quiz card unique identifier
            **data: Additional fields to set/update
            
        Returns:
            UserCard instance (created or updated)
            
        Example:
            >>> card = progress_repo.create_or_update_user_card(
            ...     user_id=42,
            ...     quiz_card_id=10,
            ...     success_count=5,
            ...     failure_count=2,
            ...     ease_factor=2.5
            ... )
            >>> progress_repo.commit()
        """
        user_card = self.get_user_card(user_id, quiz_card_id)
        
        if user_card:
            # Update existing
            for key, value in data.items():
                setattr(user_card, key, value)
        else:
            # Create new
            user_card = UserCard(
                user_id=user_id,
                quiz_card_id=quiz_card_id,
                **data
            )
            self.session.add(user_card)
        
        self.session.flush()
        return user_card

    def get_user_progress_all(self, user_id: int) -> List[UserCard]:
        """
        Get all progress records for a user.
        
        Args:
            user_id: User unique identifier
            
        Returns:
            List of all UserCard instances for the user
            
        Example:
            >>> progress = progress_repo.get_user_progress_all(42)
        """
        return (
            self.session.query(UserCard)
            .filter(UserCard.user_id == user_id)
            .all()
        )

    def get_user_progress_by_course(
        self,
        user_id: int,
        course_id: int
    ) -> List[UserCard]:
        """
        Get user progress for all quiz cards in a course.
        
        Joins with QuizCard to filter by course_id.
        
        Args:
            user_id: User unique identifier
            course_id: Course unique identifier
            
        Returns:
            List of UserCard instances for the course
            
        Example:
            >>> progress = progress_repo.get_user_progress_by_course(42, 1)
        """
        return (
            self.session.query(UserCard)
            .join(QuizCard, UserCard.quiz_card_id == QuizCard.quiz_card_id)
            .filter(
                UserCard.user_id == user_id,
                QuizCard.course_id == course_id
            )
            .all()
        )

    def get_user_progress_by_unit(
        self,
        user_id: int,
        unit_id: int
    ) -> List[UserCard]:
        """
        Get user progress for all quiz cards in a unit.
        
        Joins with QuizCard to filter by unit_id.
        
        Args:
            user_id: User unique identifier
            unit_id: Unit unique identifier
            
        Returns:
            List of UserCard instances for the unit
            
        Example:
            >>> progress = progress_repo.get_user_progress_by_unit(42, 5)
        """
        return (
            self.session.query(UserCard)
            .join(QuizCard, UserCard.quiz_card_id == QuizCard.quiz_card_id)
            .filter(
                UserCard.user_id == user_id,
                QuizCard.unit_id == unit_id
            )
            .all()
        )

    def get_user_progress_by_concept(
        self,
        user_id: int,
        concept_id: int
    ) -> List[UserCard]:
        """
        Get user progress for all quiz cards in a concept.
        
        Joins with QuizCard to filter by concept_id.
        
        Args:
            user_id: User unique identifier
            concept_id: Concept unique identifier
            
        Returns:
            List of UserCard instances for the concept
            
        Example:
            >>> progress = progress_repo.get_user_progress_by_concept(42, 10)
        """
        return (
            self.session.query(UserCard)
            .join(QuizCard, UserCard.quiz_card_id == QuizCard.quiz_card_id)
            .filter(
                UserCard.user_id == user_id,
                QuizCard.concept_id == concept_id
            )
            .all()
        )

    def get_due_cards(
        self,
        user_id: int,
        limit: Optional[int] = None
    ) -> List[UserCard]:
        """
        Get quiz cards that are due for review (spaced repetition).
        
        Args:
            user_id: User unique identifier
            limit: Optional limit on number of cards
            
        Returns:
            List of UserCard instances that are due
            
        Example:
            >>> due_cards = progress_repo.get_due_cards(42, limit=20)
        """
        query = (
            self.session.query(UserCard)
            .filter(
                UserCard.user_id == user_id,
                UserCard.due_date <= datetime.utcnow()
            )
            .order_by(UserCard.due_date)
        )
        
        if limit:
            query = query.limit(limit)
        
        return query.all()

    def count_user_cards(self, user_id: int) -> int:
        """
        Count total quiz cards seen by user.
        
        Args:
            user_id: User unique identifier
            
        Returns:
            Total number of UserCard records
            
        Example:
            >>> total = progress_repo.count_user_cards(42)
        """
        return (
            self.session.query(UserCard)
            .filter(UserCard.user_id == user_id)
            .count()
        )

    def calculate_success_rate(self, user_id: int) -> float:
        """
        Calculate overall success rate for a user.
        
        Args:
            user_id: User unique identifier
            
        Returns:
            Success rate as a float (0.0 to 1.0)
            
        Example:
            >>> rate = progress_repo.calculate_success_rate(42)
            >>> print(f"Success rate: {rate * 100:.1f}%")
        """
        result = (
            self.session.query(
                func.sum(UserCard.success_count).label('total_success'),
                func.sum(UserCard.failure_count).label('total_failure')
            )
            .filter(UserCard.user_id == user_id)
            .first()
        )
        
        total_success = result.total_success or 0
        total_failure = result.total_failure or 0
        total_attempts = total_success + total_failure
        
        if total_attempts == 0:
            return 0.0
        
        return total_success / total_attempts

    def get_cards_needing_review(
        self,
        user_id: int,
        days_back: int = 7
    ) -> List[UserCard]:
        """
        Get cards that haven't been reviewed recently.
        
        Args:
            user_id: User unique identifier
            days_back: Number of days to look back
            
        Returns:
            List of UserCard instances needing review
            
        Example:
            >>> stale_cards = progress_repo.get_cards_needing_review(42, 7)
        """
        from datetime import timedelta
        cutoff_date = datetime.utcnow() - timedelta(days=days_back)
        
        return (
            self.session.query(UserCard)
            .filter(
                UserCard.user_id == user_id,
                UserCard.last_reviewed < cutoff_date
            )
            .order_by(UserCard.last_reviewed)
            .all()
        )
