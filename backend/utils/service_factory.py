"""
Service factory for creating service instances with proper context.

This module provides factory functions to create service instances
within Flask request contexts. Services should not be instantiated
at module level as they require database sessions which need app context.

Usage:
    from backend.utils.service_factory import get_auth_service
    
    @app.route('/login')
    def login():
        auth_service = get_auth_service()
        # ... use service
"""

from backend.services.auth_service import AuthService
from backend.services.course_service import CourseService
from backend.services.quiz_service import QuizService
from backend.services.progress_service import ProgressService
from backend.repositories.user_repository import UserRepository
from backend.repositories.course_repository import CourseRepository
from backend.repositories.quiz_repository import QuizRepository
from backend.repositories.progress_repository import ProgressRepository
from backend.utils.database_manager import get_db


def get_auth_service() -> AuthService:
    """
    Get AuthService instance with current request context.
    
    Returns:
        AuthService: Configured authentication service
    """
    session = get_db()
    user_repo = UserRepository(session)
    return AuthService(user_repo)


def get_course_service() -> CourseService:
    """
    Get CourseService instance with current request context.
    
    Returns:
        CourseService: Configured course service
    """
    session = get_db()
    course_repo = CourseRepository(session)
    return CourseService(course_repo)


def get_quiz_service() -> QuizService:
    """
    Get QuizService instance with current request context.
    
    Returns:
        QuizService: Configured quiz service
    """
    session = get_db()
    quiz_repo = QuizRepository(session)
    progress_repo = ProgressRepository(session)
    return QuizService(quiz_repo, progress_repo)


def get_progress_service() -> ProgressService:
    """
    Get ProgressService instance with current request context.
    
    Returns:
        ProgressService: Configured progress service
    """
    session = get_db()
    progress_repo = ProgressRepository(session)
    return ProgressService(progress_repo)
