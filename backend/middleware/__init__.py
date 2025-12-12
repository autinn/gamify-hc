"""
Middleware - Cross-cutting concerns for request/response handling
Global error handling, request logging, authentication, and CORS
"""

from backend.middleware.error_handler import register_error_handlers
from backend.middleware.request_logger import register_request_logger
from backend.middleware.cors_middleware import register_cors

__all__ = [
    'register_error_handlers',
    'register_request_logger',
    'register_cors',
]
