"""
Schemas - Data Transfer Objects
DTOs for serialization and API responses using dataclasses
"""

from backend.schemas.auth_schemas import (
    UserResponse,
    LoginRequest,
    RegisterRequest,
    TokenResponse,
)
from backend.schemas.course_schemas import (
    CourseResponse,
    UnitResponse,
    ConceptResponse,
)
from backend.schemas.quiz_schemas import (
    QuizCardResponse,
    QuizAnswerResponse,
    QuizSubmitRequest,
    QuizSubmitResponse,
)
from backend.schemas.user_schemas import (
    UserProgressResponse,
    ProgressStatsResponse,
)

__all__ = [
    'UserResponse',
    'LoginRequest',
    'RegisterRequest',
    'TokenResponse',
    'CourseResponse',
    'UnitResponse',
    'ConceptResponse',
    'QuizCardResponse',
    'QuizAnswerResponse',
    'QuizSubmitRequest',
    'QuizSubmitResponse',
    'UserProgressResponse',
    'ProgressStatsResponse',
]
