"""
Services package for Gamify-HC backend.

This package contains business logic layer services that handle core
application functionality. Services are organized by domain entity.

Domain Packages:
    - auth: Authentication and authorization (AuthService)
    - user: User management, progress tracking
    - course: Course content hierarchy (courses, units, concepts)
    - quiz: Quiz card management (QuizService)

Architecture:
    - BaseService: Abstract base class for all services (at package root)
    - Domain packages group related services together
    - Each domain package exports its services via __init__.py

Design Principles:
    - Single Responsibility: Each service handles one domain
    - Dependency Injection: Services receive dependencies via constructor
    - Abstraction: Common patterns defined in base class
    - Testability: Services can be tested independently of Flask routes
"""

from backend.services.base_service import BaseService

# Re-export from domain packages for backward compatibility
from backend.services.auth import AuthService
from backend.services.user import UserService, UserProgressService
from backend.services.course import CourseService, UnitService, ConceptService
from backend.services.quiz import QuizService

__all__ = [
    # Base
    'BaseService',
    # Auth domain
    'AuthService',
    # User domain
    'UserService',
    'UserProgressService',
    # Course domain
    'CourseService',
    'UnitService',
    'ConceptService',
    # Quiz domain
    'QuizService',
]
