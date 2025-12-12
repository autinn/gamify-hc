"""
Graceful shutdown handler for production deployments.

This module provides signal handling for clean application shutdown:
- SIGTERM: Kubernetes/Docker container termination
- SIGINT: Ctrl+C during development

Ensures:
- In-flight HTTP requests complete
- Database connections close properly
- Resources are cleaned up
- No data loss during shutdown
"""

import atexit
import signal
import sys
import threading
from typing import Callable, Optional

from backend.utils.logger import get_logger

logger = get_logger(__name__)


class GracefulShutdown:
    """
    Handles graceful shutdown of the application.
    
    Coordinates cleanup of resources when shutdown signals are received.
    Supports multiple cleanup handlers and tracks shutdown state.
    """
    
    def __init__(self):
        """Initialize graceful shutdown handler."""
        self.shutdown_handlers: list[Callable] = []
        self.is_shutting_down = False
        self.lock = threading.Lock()
        
    def register_handler(self, handler: Callable, name: str = None):
        """
        Register a cleanup handler to run during shutdown.
        
        Args:
            handler: Callable that performs cleanup (no args)
            name: Optional name for logging
        """
        handler_name = name or getattr(
            handler, '__name__', 'unknown_handler'
        )
        self.shutdown_handlers.append((handler, handler_name))
        logger.debug(f'Registered shutdown handler: {handler_name}')
        
    def _execute_shutdown(self, signum: Optional[int] = None):
        """
        Execute all registered shutdown handlers.
        
        Args:
            signum: Signal number that triggered shutdown (or None)
        """
        with self.lock:
            if self.is_shutting_down:
                return
            self.is_shutting_down = True
        
        signal_name = (
            signal.Signals(signum).name if signum else 'NORMAL'
        )
        logger.info(f'Graceful shutdown initiated (signal: {signal_name})')
        
        # Execute handlers in reverse order (LIFO)
        for handler, name in reversed(self.shutdown_handlers):
            try:
                logger.debug(f'Executing shutdown handler: {name}')
                handler()
                logger.debug(f'Shutdown handler completed: {name}')
            except Exception as e:
                logger.error(
                    f'Error in shutdown handler {name}: {str(e)}',
                    exc_info=True
                )
        
        logger.info('Graceful shutdown completed')
    
    def _signal_handler(self, signum, frame):
        """
        Handle shutdown signals (SIGTERM, SIGINT).
        
        Args:
            signum: Signal number
            frame: Current stack frame
        """
        logger.warning(f'Received signal {signal.Signals(signum).name}')
        self._execute_shutdown(signum)
        sys.exit(0)
    
    def setup(self):
        """
        Setup signal handlers and atexit hook.
        
        Registers handlers for:
        - SIGTERM: Container/process termination
        - SIGINT: Keyboard interrupt (Ctrl+C)
        - atexit: Normal Python exit
        """
        # Handle termination signals
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGINT, self._signal_handler)
        
        # Handle normal exit
        atexit.register(lambda: self._execute_shutdown(None))
        
        logger.info('Graceful shutdown handlers registered')


# Global instance
_shutdown_handler: Optional[GracefulShutdown] = None


def get_shutdown_handler() -> GracefulShutdown:
    """
    Get or create global shutdown handler instance.
    
    Returns:
        GracefulShutdown instance
    """
    global _shutdown_handler
    if _shutdown_handler is None:
        _shutdown_handler = GracefulShutdown()
    return _shutdown_handler


def register_cleanup(handler: Callable, name: str = None):
    """
    Convenience function to register a cleanup handler.
    
    Args:
        handler: Cleanup function to execute on shutdown
        name: Optional name for logging
    """
    get_shutdown_handler().register_handler(handler, name)
