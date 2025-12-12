"""
Quiz Service - Business logic for quiz operations
Handles quiz card retrieval and spaced repetition algorithm
"""

from typing import List, Optional
from datetime import datetime, timedelta

from backend.database.models import QuizCard, UserCard
from backend.repositories.quiz_repository import QuizRepository
from backend.repositories.progress_repository import ProgressRepository
from backend.utils.logger import get_logger

logger = get_logger(__name__)


class QuizService:
    """
    Service for quiz-related operations.
    
    Handles quiz card retrieval, answer submission, and implements
    the spaced repetition algorithm for optimal learning.
    
    Example:
        >>> quiz_service = QuizService(quiz_repo, progress_repo)
        >>> cards = quiz_service.get_quiz_cards_by_course(1)
    """

    def __init__(
        self,
        quiz_repository: QuizRepository,
        progress_repository: ProgressRepository
    ):
        """
        Initialize quiz service.
        
        Args:
            quiz_repository: Quiz data access repository
            progress_repository: Progress data access repository
        """
        self.quiz_repo = quiz_repository
        self.progress_repo = progress_repository

    def get_quiz_card_by_id(
        self,
        quiz_card_id: int
    ) -> Optional[QuizCard]:
        """
        Get a quiz card with its answers.
        
        Args:
            quiz_card_id: Quiz card unique identifier
            
        Returns:
            QuizCard with answers loaded
            
        Raises:
            ValueError: If quiz card not found
        """
        logger.debug(f"Fetching quiz card: {quiz_card_id}")
        card = self.quiz_repo.get_quiz_card_with_answers(quiz_card_id)
        
        if not card:
            logger.warning(f"Quiz card not found: {quiz_card_id}")
            raise ValueError(f'Quiz card {quiz_card_id} not found')
        
        return card

    def get_quiz_cards_by_course(
        self,
        course_id: int
    ) -> List[QuizCard]:
        """
        Get all quiz cards for a course.
        
        Args:
            course_id: Course unique identifier
            
        Returns:
            List of QuizCard instances
        """
        logger.debug(f"Fetching quiz cards for course: {course_id}")
        cards = self.quiz_repo.get_quiz_cards_by_course(course_id)
        logger.info(f"Retrieved {len(cards)} cards for course {course_id}")
        return cards

    def get_quiz_cards_by_unit(self, unit_id: int) -> List[QuizCard]:
        """
        Get all quiz cards for a unit.
        
        Args:
            unit_id: Unit unique identifier
            
        Returns:
            List of QuizCard instances
        """
        logger.debug(f"Fetching quiz cards for unit: {unit_id}")
        cards = self.quiz_repo.get_quiz_cards_by_unit(unit_id)
        logger.info(f"Retrieved {len(cards)} cards for unit {unit_id}")
        return cards

    def get_quiz_cards_by_concept(
        self,
        concept_id: int
    ) -> List[QuizCard]:
        """
        Get all quiz cards for a concept.
        
        Args:
            concept_id: Concept unique identifier
            
        Returns:
            List of QuizCard instances
        """
        logger.debug(f"Fetching quiz cards for concept: {concept_id}")
        cards = self.quiz_repo.get_quiz_cards_by_concept(concept_id)
        logger.info(
            f"Retrieved {len(cards)} cards for concept {concept_id}"
        )
        return cards

    def get_all_quiz_cards(self) -> List[QuizCard]:
        """
        Get all quiz cards from all courses.
        
        Returns:
            List of all QuizCard instances
        """
        logger.debug("Fetching all quiz cards")
        cards = self.quiz_repo.get_all()
        logger.info(f"Retrieved {len(cards)} total cards")
        return cards

    def get_random_quiz_cards(self, limit: int = 10) -> List[QuizCard]:
        """
        Get random quiz cards from all courses.
        
        Args:
            limit: Maximum number of cards to return
            
        Returns:
            List of random QuizCard instances
        """
        logger.debug(f"Fetching {limit} random quiz cards")
        cards = self.quiz_repo.get_random_quiz_cards(limit)
        logger.info(f"Retrieved {len(cards)} random cards")
        return cards

    def submit_quiz_answer(
        self,
        user_id: int,
        quiz_card_id: int,
        is_correct: bool,
        is_first_attempt: bool = True
    ) -> UserCard:
        """
        Submit a quiz answer and update user progress.
        
        Implements spaced repetition algorithm to calculate
        next review date based on performance.
        
        Args:
            user_id: User unique identifier
            quiz_card_id: Quiz card unique identifier
            is_correct: Whether answer was correct
            is_first_attempt: Whether this is the first attempt (default True)
                             If False and is_correct=True, won't count as success
            
        Returns:
            Updated UserCard instance
            
        Example:
            >>> user_card = quiz_service.submit_quiz_answer(
            ...     42, 10, True, is_first_attempt=True
            ... )
            >>> print(f"Next review: {user_card.due_date}")
        """
        logger.debug(
            f"Processing quiz answer: user={user_id}, "
            f"card={quiz_card_id}, correct={is_correct}"
        )
        
        # Get or create user card
        user_card = self.progress_repo.get_user_card(
            user_id,
            quiz_card_id
        )
        
        if not user_card:
            # First time seeing this card
            user_card = self._create_new_user_card(
                user_id,
                quiz_card_id,
                is_correct,
                is_first_attempt
            )
        else:
            # Update existing card
            user_card = self._update_user_card(
                user_card, is_correct, is_first_attempt
            )
        
        self.progress_repo.commit()
        
        logger.info(
            f"Quiz answer processed: user={user_id}, "
            f"card={quiz_card_id}, "
            f"next_review_days={user_card.interval_days}"
        )
        
        return user_card

    def _create_new_user_card(
        self,
        user_id: int,
        quiz_card_id: int,
        is_correct: bool,
        is_first_attempt: bool = True
    ) -> UserCard:
        """Create a new UserCard for first-time quiz attempt."""
        now = datetime.utcnow()
        
        # Only count as success if correct AND first attempt
        counts_as_success = is_correct and is_first_attempt
        
        if counts_as_success:
            # First success: review in 1 day
            interval_days = 1
            ease_factor = 2.5
            success_count = 1
            failure_count = 0
            repetitions = 1
        else:
            # First failure or retry: review immediately
            interval_days = 0
            ease_factor = 2.5
            success_count = 0
            # Only count as failure if it's a first attempt
            failure_count = 1 if is_first_attempt else 0
            # Always count as seen (repetitions = 1)
            repetitions = 1
        
        due_date = now + timedelta(days=interval_days)
        
        return self.progress_repo.create_or_update_user_card(
            user_id=user_id,
            quiz_card_id=quiz_card_id,
            ease_factor=ease_factor,
            interval_days=interval_days,
            due_date=due_date,
            last_reviewed=now,
            repetitions=repetitions,
            success_count=success_count,
            failure_count=failure_count
        )

    def _update_user_card(
        self,
        user_card: UserCard,
        is_correct: bool,
        is_first_attempt: bool = True
    ) -> UserCard:
        """Update existing UserCard using spaced repetition algorithm."""
        now = datetime.utcnow()
        
        # Always increment repetitions to track times seen
        user_card.repetitions += 1
        
        # Only count as success if correct AND first attempt
        counts_as_success = is_correct and is_first_attempt
        
        # Update success/failure counts
        if counts_as_success:
            user_card.success_count += 1
        elif not is_correct and is_first_attempt:
            # Only count as failure if it's a first attempt
            user_card.failure_count += 1
        # If not first attempt, don't update success/failure counts
        
        # Calculate new ease factor and interval
        user_card.ease_factor, user_card.interval_days = (
            self._calculate_next_interval(
                user_card.ease_factor,
                user_card.interval_days,
                user_card.repetitions,
                counts_as_success
            )
        )
        
        # Calculate next due date
        user_card.due_date = now + timedelta(days=user_card.interval_days)
        user_card.last_reviewed = now
        
        self.progress_repo.session.flush()
        
        return user_card

    def _calculate_next_interval(
        self,
        ease_factor: float,
        current_interval: int,
        repetitions: int,
        is_correct: bool
    ) -> tuple[float, int]:
        """
        Calculate next review interval using spaced repetition.
        
        Based on SM-2 algorithm (SuperMemo 2).
        
        Args:
            ease_factor: Current ease factor (1.3-3.0)
            current_interval: Current interval in days
            repetitions: Number of consecutive successes
            is_correct: Whether last answer was correct
            
        Returns:
            Tuple of (new_ease_factor, new_interval_days)
        """
        if not is_correct:
            # Reset interval on failure
            new_ease_factor = max(1.3, ease_factor - 0.2)
            new_interval = 0  # Review immediately
            return new_ease_factor, new_interval
        
        # Increase ease factor on success
        new_ease_factor = min(3.0, ease_factor + 0.1)
        
        # Calculate new interval based on repetitions
        if repetitions == 1:
            new_interval = 1
        elif repetitions == 2:
            new_interval = 6
        else:
            # Exponential growth for subsequent reviews
            new_interval = int(current_interval * new_ease_factor)
        
        return new_ease_factor, new_interval

    def get_due_cards_for_user(
        self,
        user_id: int,
        limit: Optional[int] = None
    ) -> List[UserCard]:
        """
        Get quiz cards due for review.
        
        Args:
            user_id: User unique identifier
            limit: Optional limit on number of cards
            
        Returns:
            List of UserCard instances that are due
        """
        logger.debug(f"Fetching due cards for user: {user_id}")
        due_cards = self.progress_repo.get_due_cards(user_id, limit)
        logger.info(
            f"User {user_id} has {len(due_cards)} cards due"
        )
        return due_cards

    def check_answer_correctness(self, answer_id: int) -> bool:
        """
        Check if a quiz answer is correct.
        
        Args:
            answer_id: Answer unique identifier
            
        Returns:
            True if answer is correct, False otherwise
            
        Raises:
            ValueError: If answer not found
        """
        answer = self.quiz_repo.get_answer_by_id(answer_id)
        if not answer:
            raise ValueError(f'Answer {answer_id} not found')
        return answer.is_correct

    def get_answer_explanation(self, answer_id: int) -> Optional[str]:
        """
        Get explanation for an answer.
        
        Args:
            answer_id: Answer unique identifier
            
        Returns:
            Explanation string or None
            
        Raises:
            ValueError: If answer not found
        """
        answer = self.quiz_repo.get_answer_by_id(answer_id)
        if not answer:
            raise ValueError(f'Answer {answer_id} not found')
        return answer.explanation
