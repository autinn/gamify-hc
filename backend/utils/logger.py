"""
Structured Logging Configuration - 12-Factor App Compliant
Logs as event streams to stdout/stderr
"""

import logging
import sys
import json
from datetime import datetime
from typing import Any, Dict, Optional
import traceback


class JSONFormatter(logging.Formatter):
    """
    JSON formatter for structured logging in production.
    
    Outputs log records as JSON for easy parsing by log aggregation
    systems like ELK, Splunk, CloudWatch, etc.
    """

    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON."""
        log_data: Dict[str, Any] = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
        }

        # Add exception info if present
        if record.exc_info:
            log_data['exception'] = {
                'type': record.exc_info[0].__name__,
                'message': str(record.exc_info[1]),
                'traceback': traceback.format_exception(*record.exc_info)
            }

        # Add extra fields from record
        if hasattr(record, 'request_id'):
            log_data['request_id'] = record.request_id
        if hasattr(record, 'user_id'):
            log_data['user_id'] = record.user_id
        if hasattr(record, 'endpoint'):
            log_data['endpoint'] = record.endpoint
        if hasattr(record, 'method'):
            log_data['method'] = record.method
        if hasattr(record, 'status_code'):
            log_data['status_code'] = record.status_code
        if hasattr(record, 'duration_ms'):
            log_data['duration_ms'] = record.duration_ms

        return json.dumps(log_data)


class ColoredTextFormatter(logging.Formatter):
    """
    Human-readable colored formatter for development.
    
    Adds colors to different log levels for better visibility
    during development.
    """

    # ANSI color codes
    COLORS = {
        'DEBUG': '\033[36m',      # Cyan
        'INFO': '\033[32m',       # Green
        'WARNING': '\033[33m',    # Yellow
        'ERROR': '\033[31m',      # Red
        'CRITICAL': '\033[35m',   # Magenta
    }
    RESET = '\033[0m'
    BOLD = '\033[1m'

    def format(self, record: logging.LogRecord) -> str:
        """Format log record with colors."""
        color = self.COLORS.get(record.levelname, self.RESET)
        
        # Format: [TIMESTAMP] LEVEL - module.function:line - message
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = f"{color}{self.BOLD}{record.levelname}{self.RESET}"
        location = f"{record.module}.{record.funcName}:{record.lineno}"
        message = record.getMessage()
        
        log_line = f"[{timestamp}] {level} - {location} - {message}"
        
        # Add exception info if present
        if record.exc_info:
            log_line += '\n' + self.formatException(record.exc_info)
        
        return log_line


def setup_logging(
    log_level: str = "INFO",
    log_format: str = "text",
    app_name: str = "gamify-hc"
) -> logging.Logger:
    """
    Setup application logging following 12-Factor principles.
    
    Logs are written to stdout (INFO and below) and stderr (WARNING and
    above) as event streams. The execution environment handles log
    aggregation and storage.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_format: Format type ('json' for production, 'text' for dev)
        app_name: Application name for logger
        
    Returns:
        logging.Logger: Configured root logger
        
    Example:
        >>> from backend.utils.logger import setup_logging
        >>> logger = setup_logging('INFO', 'json', 'gamify-hc')
        >>> logger.info('Application started')
    """
    # Get root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    # Remove existing handlers
    root_logger.handlers.clear()
    
    # Choose formatter based on environment
    if log_format == "json":
        formatter = JSONFormatter()
    else:
        formatter = ColoredTextFormatter()
    
    # Handler for INFO and below -> stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(lambda record: record.levelno <= logging.INFO)
    stdout_handler.setFormatter(formatter)
    
    # Handler for WARNING and above -> stderr
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.WARNING)
    stderr_handler.setFormatter(formatter)
    
    # Add handlers
    root_logger.addHandler(stdout_handler)
    root_logger.addHandler(stderr_handler)
    
    # Create app logger
    app_logger = logging.getLogger(app_name)
    
    return app_logger


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance.
    
    Args:
        name: Logger name (usually __name__ of the module)
        
    Returns:
        logging.Logger: Logger instance
        
    Example:
        >>> from backend.utils.logger import get_logger
        >>> logger = get_logger(__name__)
        >>> logger.info('Processing request')
    """
    return logging.getLogger(name or 'gamify-hc')


class LogContext:
    """
    Context manager for adding context to log records.
    
    This allows adding request-specific information (like request_id,
    user_id) to all log messages within a context.
    
    Example:
        >>> with LogContext(request_id='abc-123', user_id=42):
        >>>     logger.info('User action')
        # Logs will include request_id and user_id
    """

    def __init__(self, **kwargs):
        """Initialize with context data."""
        self.context = kwargs
        self.old_factory = None

    def __enter__(self):
        """Enter context and add fields to log records."""
        old_factory = logging.getLogRecordFactory()
        self.old_factory = old_factory

        def record_factory(*args, **kwargs):
            record = old_factory(*args, **kwargs)
            for key, value in self.context.items():
                setattr(record, key, value)
            return record

        logging.setLogRecordFactory(record_factory)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context and restore original factory."""
        if self.old_factory:
            logging.setLogRecordFactory(self.old_factory)


# Convenience function for request logging
def log_request(
    logger: logging.Logger,
    method: str,
    endpoint: str,
    status_code: int,
    duration_ms: float,
    request_id: Optional[str] = None,
    user_id: Optional[int] = None
):
    """
    Log an HTTP request with structured data.
    
    Args:
        logger: Logger instance
        method: HTTP method (GET, POST, etc.)
        endpoint: Request endpoint
        status_code: Response status code
        duration_ms: Request duration in milliseconds
        request_id: Optional request ID
        user_id: Optional user ID
        
    Example:
        >>> log_request(
        ...     logger, 'GET', '/api/courses', 200, 45.3,
        ...     request_id='abc-123', user_id=42
        ... )
    """
    extra = {
        'method': method,
        'endpoint': endpoint,
        'status_code': status_code,
        'duration_ms': duration_ms,
    }
    if request_id:
        extra['request_id'] = request_id
    if user_id:
        extra['user_id'] = user_id
    
    level = logging.INFO if status_code < 400 else logging.WARNING
    logger.log(
        level,
        f"{method} {endpoint} {status_code} ({duration_ms:.2f}ms)",
        extra=extra
    )
