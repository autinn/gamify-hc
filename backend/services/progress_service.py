"""
Progress Service - Business logic for user progress tracking
Handles progress analytics and aggregations
"""

from typing import Dict, List

from backend.database.models import UserCard
from backend.repositories.progress_repository import ProgressRepository
from backend.repositories.quiz_repository import QuizRepository
from backend.utils.logger import get_logger

logger = get_logger(__name__)


class ProgressService:
    """
    Service for progress tracking and analytics.
    
    Handles user progress queries, aggregations by course/unit/concept,
    and success rate calculations.
    
    Example:
        >>> progress_service = ProgressService(progress_repo, quiz_repo)
        >>> stats = progress_service.get_user_progress_summary(42)
    """

    def __init__(
        self,
        progress_repository: ProgressRepository,
        quiz_repository: QuizRepository
    ):
        """
        Initialize progress service.
        
        Args:
            progress_repository: Progress data access repository
            quiz_repository: Quiz data access repository
        """
        self.progress_repo = progress_repository
        self.quiz_repo = quiz_repository

    def get_user_progress_all(self, user_id: int) -> List[UserCard]:
        """
        Get all progress records for a user.
        
        Args:
            user_id: User unique identifier
            
        Returns:
            List of all UserCard instances
        """
        logger.debug(f"Fetching all progress for user: {user_id}")
        progress = self.progress_repo.get_user_progress_all(user_id)
        logger.info(f"User {user_id} has {len(progress)} cards tracked")
        return progress

    def get_user_progress_summary(self, user_id: int) -> Dict:
        """
        Get overall progress summary for a user.
        
        Args:
            user_id: User unique identifier
            
        Returns:
            Dictionary with summary statistics
            
        Example:
            >>> summary = progress_service.get_user_progress_summary(42)
            >>> print(f"Success rate: {summary['success_rate']:.1%}")
        """
        logger.debug(f"Calculating progress summary for user: {user_id}")
        
        # Get all progress records
        all_progress = self.progress_repo.get_user_progress_all(user_id)
        
        # Calculate statistics
        total_cards = len(all_progress)
        total_success = sum(p.success_count for p in all_progress)
        total_failure = sum(p.failure_count for p in all_progress)
        total_attempts = total_success + total_failure
        
        success_rate = (
            total_success / total_attempts if total_attempts > 0 else 0.0
        )
        
        # Count cards by status
        due_count = sum(
            1 for p in all_progress
            if p.due_date and p.due_date <= self._now()
        )
        
        summary = {
            'total_cards_seen': total_cards,
            'total_attempts': total_attempts,
            'total_success': total_success,
            'total_failure': total_failure,
            'success_rate': success_rate,
            'cards_due_for_review': due_count,
        }
        
        logger.info(
            f"Progress summary for user {user_id}: "
            f"{total_cards} cards, {success_rate:.1%} success rate"
        )
        
        return summary

    def get_course_progress(
        self,
        user_id: int,
        course_id: int
    ) -> Dict:
        """
        Get progress statistics for a specific course.
        
        Args:
            user_id: User unique identifier
            course_id: Course unique identifier
            
        Returns:
            Dictionary with course progress statistics
        """
        logger.debug(
            f"Fetching course progress: "
            f"user={user_id}, course={course_id}"
        )
        
        # Get progress for this course
        progress = self.progress_repo.get_user_progress_by_course(
            user_id,
            course_id
        )
        
        # Get total cards in course
        total_cards = self.quiz_repo.get_quiz_card_count_by_course(
            course_id
        )
        
        # Calculate statistics
        stats = self._calculate_stats(progress, total_cards)
        stats['course_id'] = course_id
        
        logger.info(
            f"Course {course_id} progress for user {user_id}: "
            f"{stats['cards_seen']}/{stats['total_cards']} cards"
        )
        
        return stats

    def get_unit_progress(self, user_id: int, unit_id: int) -> Dict:
        """
        Get progress statistics for a specific unit.
        
        Args:
            user_id: User unique identifier
            unit_id: Unit unique identifier
            
        Returns:
            Dictionary with unit progress statistics
        """
        logger.debug(
            f"Fetching unit progress: user={user_id}, unit={unit_id}"
        )
        
        # Get progress for this unit
        progress = self.progress_repo.get_user_progress_by_unit(
            user_id,
            unit_id
        )
        
        # Get total cards in unit
        total_cards = self.quiz_repo.get_quiz_card_count_by_unit(unit_id)
        
        # Calculate statistics
        stats = self._calculate_stats(progress, total_cards)
        stats['unit_id'] = unit_id
        
        logger.info(
            f"Unit {unit_id} progress for user {user_id}: "
            f"{stats['cards_seen']}/{stats['total_cards']} cards"
        )
        
        return stats

    def get_concept_progress(
        self,
        user_id: int,
        concept_id: int
    ) -> Dict:
        """
        Get progress statistics for a specific concept.
        
        Args:
            user_id: User unique identifier
            concept_id: Concept unique identifier
            
        Returns:
            Dictionary with concept progress statistics
        """
        logger.debug(
            f"Fetching concept progress: "
            f"user={user_id}, concept={concept_id}"
        )
        
        # Get progress for this concept
        progress = self.progress_repo.get_user_progress_by_concept(
            user_id,
            concept_id
        )
        
        # Get total cards in concept
        total_cards = self.quiz_repo.get_quiz_card_count_by_concept(
            concept_id
        )
        
        # Calculate statistics
        stats = self._calculate_stats(progress, total_cards)
        stats['concept_id'] = concept_id
        
        logger.info(
            f"Concept {concept_id} progress for user {user_id}: "
            f"{stats['cards_seen']}/{stats['total_cards']} cards"
        )
        
        return stats

    def get_all_courses_progress(self, user_id: int) -> List[Dict]:
        """
        Get progress summary for all courses.
        
        Args:
            user_id: User unique identifier
            
        Returns:
            List of dictionaries, one per course
        """
        logger.debug(f"Fetching all course progress for user: {user_id}")
        
        # This would need CourseRepository to get all courses
        # For now, return empty list
        # TODO: Inject CourseRepository and implement
        logger.warning(
            "get_all_courses_progress not fully implemented"
        )
        return []

    def get_courses_progress_chart_data(self, user_id: int) -> Dict:
        """
        Get chart-formatted progress data for all courses.
        
        Returns data in format suitable for frontend charts:
        {labels: ['Course 1', 'Course 2'], values: [0.75, 0.82]}
        
        Args:
            user_id: User unique identifier
            
        Returns:
            Dictionary with labels and values arrays
        """
        logger.debug(
            f"Fetching chart data for all courses: user={user_id}"
        )
        
        try:
            # Get all courses with quiz cards
            from backend.repositories.course_repository import (
                CourseRepository
            )
            course_repo = CourseRepository(self.progress_repo.session)
            all_courses = course_repo.get_all_courses()
            
            labels = []
            values = []
            
            for course in all_courses:
                # Get progress for this course
                progress = self.progress_repo.get_user_progress_by_course(
                    user_id, course.course_id
                )
                
                # Calculate success rate using repetitions (total attempts)
                total_success = sum(p.success_count for p in progress)
                total_repetitions = sum(p.repetitions for p in progress)
                
                success_rate = (
                    total_success / total_repetitions
                    if total_repetitions > 0 else 0.0
                )
                
                labels.append(course.title)
                values.append(success_rate)
            
            return {
                'labels': labels,
                'values': values,
                'metadata': {
                    'type': 'courses',
                    'user_id': user_id
                }
            }
        except Exception as e:
            logger.error(f"Error fetching courses chart data: {str(e)}")
            return {'labels': [], 'values': [], 'metadata': {}}

    def get_units_progress_chart_data(
        self, user_id: int, course_id: int
    ) -> Dict:
        """
        Get chart-formatted progress data for all units in a course.
        
        Args:
            user_id: User unique identifier
            course_id: Course unique identifier
            
        Returns:
            Dictionary with labels and values arrays
        """
        logger.debug(
            f"Fetching chart data for course units: "
            f"user={user_id}, course={course_id}"
        )
        
        try:
            # Get all units in the course
            from backend.repositories.course_repository import (
                CourseRepository
            )
            course_repo = CourseRepository(self.progress_repo.session)
            units = course_repo.get_units_by_course(course_id)
            
            labels = []
            values = []
            
            for unit in units:
                # Get progress for this unit
                progress = self.progress_repo.get_user_progress_by_unit(
                    user_id, unit.unit_id
                )
                
                # Calculate success rate using repetitions (total attempts)
                total_success = sum(p.success_count for p in progress)
                total_repetitions = sum(p.repetitions for p in progress)
                
                success_rate = (
                    total_success / total_repetitions
                    if total_repetitions > 0 else 0.0
                )
                
                labels.append(unit.title)
                values.append(success_rate)
            
            return {
                'labels': labels,
                'values': values,
                'metadata': {
                    'type': 'units',
                    'user_id': user_id,
                    'course_id': course_id
                }
            }
        except Exception as e:
            logger.error(f"Error fetching units chart data: {str(e)}")
            return {'labels': [], 'values': [], 'metadata': {}}

    def get_concepts_progress_chart_data(
        self, user_id: int, course_id: int, unit_id: int
    ) -> Dict:
        """
        Get chart-formatted progress data for all concepts in a unit.
        
        Args:
            user_id: User unique identifier
            course_id: Course unique identifier (for context)
            unit_id: Unit unique identifier
            
        Returns:
            Dictionary with labels and values arrays
        """
        logger.debug(
            f"Fetching chart data for unit concepts: "
            f"user={user_id}, unit={unit_id}"
        )
        
        try:
            # Get all concepts in the unit
            from backend.repositories.course_repository import (
                CourseRepository
            )
            course_repo = CourseRepository(self.progress_repo.session)
            concepts = course_repo.get_concepts_by_unit(unit_id)
            
            labels = []
            values = []
            
            for concept in concepts:
                # Get progress for this concept
                progress = self.progress_repo.get_user_progress_by_concept(
                    user_id, concept.concept_id
                )
                
                # Calculate success rate using repetitions (total attempts)
                total_success = sum(p.success_count for p in progress)
                total_repetitions = sum(p.repetitions for p in progress)
                
                success_rate = (
                    total_success / total_repetitions
                    if total_repetitions > 0 else 0.0
                )
                
                labels.append(concept.title)
                values.append(success_rate)
            
            return {
                'labels': labels,
                'values': values,
                'metadata': {
                    'type': 'concepts',
                    'user_id': user_id,
                    'course_id': course_id,
                    'unit_id': unit_id
                }
            }
        except Exception as e:
            logger.error(f"Error fetching concepts chart data: {str(e)}")
            return {'labels': [], 'values': [], 'metadata': {}}

    def _calculate_stats(
        self,
        progress: List[UserCard],
        total_cards: int
    ) -> Dict:
        """
        Calculate statistics from progress records.
        
        Args:
            progress: List of UserCard instances
            total_cards: Total cards available
            
        Returns:
            Dictionary with calculated statistics
        """
        cards_seen = len(progress)
        total_success = sum(p.success_count for p in progress)
        total_failure = sum(p.failure_count for p in progress)
        total_attempts = total_success + total_failure
        
        success_rate = (
            total_success / total_attempts if total_attempts > 0 else 0.0
        )
        
        completion_rate = (
            cards_seen / total_cards if total_cards > 0 else 0.0
        )
        
        return {
            'total_cards': total_cards,
            'cards_seen': cards_seen,
            'cards_not_seen': total_cards - cards_seen,
            'total_attempts': total_attempts,
            'success_count': total_success,
            'failure_count': total_failure,
            'success_rate': success_rate,
            'completion_rate': completion_rate,
        }

    def _now(self):
        """Get current UTC datetime (for easier testing)."""
        from datetime import datetime
        return datetime.utcnow()
