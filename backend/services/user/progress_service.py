"""
User Progress Service Module.

This module provides business logic for user progress tracking, including
quiz card progress, onboarding status, and hierarchical progress aggregation
by courses, units, and concepts.

Classes:
    UserProgressService: Service for managing user progress operations
"""

from typing import Optional, List, Dict, Any
from sqlalchemy import func

from backend.database.models import (
    User, UserCard, QuizCard, Concept, Unit, Course
)
from backend.services.base_service import BaseService


class UserProgressService(BaseService):
    """
    Service for user progress management operations.
    
    This service handles:
    - User quiz card progress tracking
    - Onboarding status management
    - Progress aggregation by courses, units, and concepts
    - Success rate calculations
    
    Inherits from BaseService for common database operations.
    
    Example:
        progress_service = UserProgressService(db_session=db)
        progress = progress_service.get_user_quiz_progress(user_id=1)
    """
    
    def get_user_quiz_progress(self, user_id: int) -> List[Dict[str, Any]]:
        """
        Get all quiz card progress for a user.
        
        Retrieves UserCard records showing how many times the user has
        seen each quiz card, how many times they answered correctly,
        and when they last reviewed it.
        
        Args:
            user_id: The user's unique identifier
        
        Returns:
            List of progress dictionaries with structure:
            [{
                'quiz_card_id': int,
                'times_seen': int,
                'times_correct': int,
                'last_seen': str (ISO format) or None
            }, ...]
            
        Raises:
            ValueError: If database session is not initialized
            
        Example:
            progress = progress_service.get_user_quiz_progress(1)
            for card in progress:
                print(f"Card {card['quiz_card_id']}: "
                      f"{card['times_correct']}/{card['times_seen']}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        # Query all progress records for user
        user_cards = self.db_session.query(UserCard).filter(
            UserCard.user_id == user_id
        ).all()
        
        # Transform to JSON-serializable format
        return [{
            'quiz_card_id': uc.quiz_card_id,
            'times_seen': uc.success_count + uc.failure_count,
            'times_correct': uc.success_count,
            'last_seen': (
                uc.last_reviewed.isoformat()
                if uc.last_reviewed else None
            )
        } for uc in user_cards]
    
    def get_onboarding_status(self, user_id: int) -> Optional[Dict[str, Any]]:
        """
        Get user's onboarding completion status.
        
        Args:
            user_id: The user's unique identifier
        
        Returns:
            Dictionary with user_id and has_completed_onboarding,
            or None if user not found
            
        Example:
            status = progress_service.get_onboarding_status(1)
            if status and not status['has_completed_onboarding']:
                print("User needs to complete onboarding")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        user = self.db_session.query(User).filter(
            User.user_id == user_id
        ).first()
        
        if not user:
            return None
        
        return {
            'user_id': user.user_id,
            'has_completed_onboarding': user.has_completed_onboarding
        }
    
    def update_onboarding_status(
        self,
        user_id: int,
        has_completed: bool
    ) -> Optional[Dict[str, Any]]:
        """
        Update user's onboarding completion status.
        
        Args:
            user_id: The user's unique identifier
            has_completed: True to mark onboarding as completed
        
        Returns:
            Dictionary with updated user_id and has_completed_onboarding,
            or None if user not found
            
        Example:
            result = progress_service.update_onboarding_status(
                user_id=1,
                has_completed=True
            )
            if result:
                print(f"Onboarding status updated: {result}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        user = self.db_session.query(User).filter(
            User.user_id == user_id
        ).first()
        
        if not user:
            return None
        
        user.has_completed_onboarding = has_completed
        self.save(user, commit=True)
        
        return {
            'user_id': user.user_id,
            'has_completed_onboarding': user.has_completed_onboarding
        }
    
    def get_courses_progress(self, user_id: int) -> Dict[str, Any]:
        """
        Get user's progress aggregated by courses.
        
        Calculates success rate for each course based on the user's
        quiz card attempts. Uses denormalized course_id from QuizCard
        for optimized querying.
        
        Args:
            user_id: The user's unique identifier
        
        Returns:
            Dictionary with structure:
            {
                'labels': ['Course 1', 'Course 2', ...],
                'values': [0.8, 0.6, ...],  # success rate (0.0 to 1.0)
                'metadata': {
                    'type': 'courses',
                    'count': int,
                    'timestamp': None
                }
            }
            
        Example:
            data = progress_service.get_courses_progress(1)
            for label, value in zip(data['labels'], data['values']):
                print(f"{label}: {value*100:.0f}% success")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        # Query aggregated by course
        # Uses QuizCard.course_id (denormalized) for direct join
        results = self.db_session.query(
            Course.title,
            func.sum(UserCard.success_count).label('total_success'),
            func.sum(UserCard.repetitions).label('total_repetitions')
        ).join(
            QuizCard, UserCard.quiz_card_id == QuizCard.quiz_card_id
        ).join(
            Course, QuizCard.course_id == Course.course_id
        ).filter(
            UserCard.user_id == user_id
        ).group_by(
            QuizCard.course_id, Course.title
        ).order_by(
            QuizCard.course_id
        ).all()
        
        # Transform to chart-friendly format
        labels = [r[0] for r in results]
        values = []
        for r in results:
            success = r[1] or 0
            total = r[2] or 0
            rate = success / total if total > 0 else 0
            values.append(round(rate, 2))
        
        return {
            'labels': labels,
            'values': values,
            'metadata': {
                'type': 'courses',
                'count': len(labels),
                'timestamp': None
            }
        }
    
    def get_units_progress(
        self,
        user_id: int,
        course_id: int
    ) -> Dict[str, Any]:
        """
        Get user's progress aggregated by units in a course.
        
        Calculates success rate for each unit in the specified course.
        Uses denormalized unit_id from QuizCard for optimized querying.
        
        Args:
            user_id: The user's unique identifier
            course_id: The course ID to filter units
        
        Returns:
            Dictionary with structure:
            {
                'labels': ['Unit 1', 'Unit 2', ...],
                'values': [0.8, 0.6, ...],  # success rate per unit
                'metadata': {
                    'type': 'units',
                    'course_id': int,
                    'count': int,
                    'timestamp': None
                }
            }
            
        Example:
            data = progress_service.get_units_progress(1, course_id=1)
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        # Query aggregated by unit within course
        results = self.db_session.query(
            Unit.order_index,
            Unit.title,
            func.sum(UserCard.success_count).label('total_success'),
            func.sum(UserCard.repetitions).label('total_repetitions')
        ).join(
            QuizCard, UserCard.quiz_card_id == QuizCard.quiz_card_id
        ).join(
            Unit, QuizCard.unit_id == Unit.unit_id
        ).filter(
            UserCard.user_id == user_id,
            QuizCard.course_id == course_id
        ).group_by(
            QuizCard.unit_id, Unit.order_index, Unit.title
        ).order_by(
            Unit.order_index
        ).all()
        
        # Format labels as "Unit 1", "Unit 2", etc.
        labels = [
            f"Unit {r[0] + 1}" if r[0] is not None else r[1]
            for r in results
        ]
        values = []
        for r in results:
            success = r[2] or 0
            total = r[3] or 0
            rate = success / total if total > 0 else 0
            values.append(round(rate, 2))
        
        return {
            'labels': labels,
            'values': values,
            'metadata': {
                'type': 'units',
                'course_id': course_id,
                'count': len(labels),
                'timestamp': None
            }
        }
    
    def get_concepts_progress(
        self,
        user_id: int,
        unit_id: int,
        course_id: int
    ) -> Dict[str, Any]:
        """
        Get user's progress aggregated by concepts in a unit.
        
        Calculates success rate for each concept in the specified unit.
        
        Args:
            user_id: The user's unique identifier
            unit_id: The unit ID to filter concepts
            course_id: The course ID (for metadata)
        
        Returns:
            Dictionary with structure:
            {
                'labels': ['Concept 1', 'Concept 2', ...],
                'values': [0.8, 0.6, ...],  # success rate per concept
                'metadata': {
                    'type': 'concepts',
                    'course_id': int,
                    'unit_id': int,
                    'count': int,
                    'timestamp': None
                }
            }
            
        Example:
            data = progress_service.get_concepts_progress(
                user_id=1,
                unit_id=1,
                course_id=1
            )
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        # Query aggregated by concept within unit
        results = self.db_session.query(
            Concept.title,
            func.sum(UserCard.success_count).label('total_success'),
            func.sum(UserCard.repetitions).label('total_repetitions')
        ).join(
            QuizCard, UserCard.quiz_card_id == QuizCard.quiz_card_id
        ).join(
            Concept, QuizCard.concept_id == Concept.concept_id
        ).filter(
            UserCard.user_id == user_id,
            Concept.unit_id == unit_id
        ).group_by(
            Concept.concept_id, Concept.title
        ).order_by(
            Concept.concept_id
        ).all()
        
        # Transform to chart-friendly format
        labels = [r[0] for r in results]
        values = []
        for r in results:
            success = r[1] or 0
            total = r[2] or 0
            rate = success / total if total > 0 else 0
            values.append(round(rate, 2))
        
        return {
            'labels': labels,
            'values': values,
            'metadata': {
                'type': 'concepts',
                'course_id': course_id,
                'unit_id': unit_id,
                'count': len(labels),
                'timestamp': None
            }
        }
