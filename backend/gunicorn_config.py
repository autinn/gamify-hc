"""
Gunicorn Configuration for Production WSGI Server
Implements 12-Factor App concurrency principles
"""

import multiprocessing
import os

# Bind to host and port from environment
bind = f"{os.getenv('SERVER_HOST', '0.0.0.0')}:{os.getenv('SERVER_PORT', '5001')}"

# Worker processes (2-4 per CPU core recommended)
workers = int(os.getenv('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1))

# Worker class - sync for CPU-bound, gevent/eventlet for I/O-bound
worker_class = os.getenv('GUNICORN_WORKER_CLASS', 'sync')

# Threads per worker (for sync workers)
threads = int(os.getenv('GUNICORN_THREADS', 2))

# Max requests per worker before restart (prevents memory leaks)
max_requests = int(os.getenv('GUNICORN_MAX_REQUESTS', 1000))
max_requests_jitter = int(os.getenv('GUNICORN_MAX_REQUESTS_JITTER', 50))

# Timeout for requests (30 seconds default)
timeout = int(os.getenv('GUNICORN_TIMEOUT', 30))

# Graceful timeout for workers (30 seconds)
graceful_timeout = int(os.getenv('GUNICORN_GRACEFUL_TIMEOUT', 30))

# Keep-alive connections
keepalive = int(os.getenv('GUNICORN_KEEPALIVE', 5))

# Logging
accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stderr
loglevel = os.getenv('LOG_LEVEL', 'info').lower()
access_log_format = (
    '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s '
    '"%(f)s" "%(a)s" %(D)s'
)

# Preload application for faster worker spawning
preload_app = True

# Worker restart on code changes (development only)
reload = os.getenv('ENVIRONMENT', 'production').lower() == 'development'

# Process naming
proc_name = 'gamify-hc-api'

# Server mechanics
daemon = False  # Run in foreground (for Docker)
pidfile = None  # No PID file needed in containers
umask = 0
user = None
group = None
tmp_upload_dir = None


def on_starting(server):
    """Called just before the master process starts."""
    server.log.info("Gunicorn master process starting")


def when_ready(server):
    """Called just after the server is started."""
    server.log.info(
        f"Gunicorn ready with {workers} workers on {bind}"
    )


def on_reload(server):
    """Called to recycle workers during a reload via SIGHUP."""
    server.log.info("Gunicorn reloading workers")


def worker_int(worker):
    """Called when a worker receives a SIGINT or SIGQUIT signal."""
    worker.log.info(f"Worker {worker.pid} received interrupt signal")


def worker_abort(worker):
    """Called when a worker receives a SIGABRT signal."""
    worker.log.warning(f"Worker {worker.pid} aborted")


def pre_fork(server, worker):
    """Called just before a worker is forked."""
    pass


def post_fork(server, worker):
    """Called just after a worker has been forked."""
    server.log.info(f"Worker {worker.pid} spawned")


def post_worker_init(worker):
    """Called just after a worker has initialized the application."""
    worker.log.info(f"Worker {worker.pid} initialized")


def worker_exit(server, worker):
    """Called just after a worker has been exited."""
    server.log.info(f"Worker {worker.pid} exited")


def on_exit(server):
    """Called just before the master process exits."""
    server.log.info("Gunicorn master process shutting down")
