"""
Repository Layer - Data Access Objects
Centralized database query logic following Repository Pattern
"""

from backend.repositories.base_repository import BaseRepository
from backend.repositories.user_repository import UserRepository
from backend.repositories.course_repository import CourseRepository
from backend.repositories.quiz_repository import QuizRepository
from backend.repositories.progress_repository import ProgressRepository

__all__ = [
    'BaseRepository',
    'UserRepository',
    'CourseRepository',
    'QuizRepository',
    'ProgressRepository',
]
