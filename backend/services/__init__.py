"""
Services package for Gamify-HC backend.

This package contains business logic layer services that handle core
application functionality. Services are separated from route handlers to
promote separation of concerns, testability, and reusability.

Architecture:
    - BaseService: Abstract base class for all services
    - AuthService: Authentication and authorization logic
    - UserService: User management operations
    - Additional services can inherit from BaseService

Design Principles:
    - Single Responsibility: Each service handles one domain
    - Dependency Injection: Services receive dependencies via constructor
    - Abstraction: Common patterns defined in base class
    - Testability: Services can be tested independently of Flask routes
"""

from backend.services.base_service import BaseService
from backend.services.auth_service import AuthService
from backend.services.user_service import UserService

__all__ = [
    'BaseService',
    'AuthService',
    'UserService',
]
