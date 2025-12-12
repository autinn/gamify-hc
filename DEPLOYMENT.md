# Deployment Guide

This guide covers deployment strategies for the Gamify-HC application following 12-Factor App principles.

## Table of Contents
- [Health Check Endpoints](#health-check-endpoints)
- [Platform Deployment (Heroku/Railway)](#platform-deployment-herokurailway)
- [Container Deployment (Docker/Kubernetes)](#container-deployment-dockerkubernetes)
- [Scaling Strategy](#scaling-strategy)
- [Environment Configuration](#environment-configuration)

---

## Health Check Endpoints

The application provides three health check endpoints for monitoring and orchestration:

### `/api/health` - Comprehensive Health Status

Returns detailed information including database connectivity, version, and uptime.

**Response (200 OK):**
```json
{
  "status": "ok",
  "timestamp": "2025-12-11T10:30:45Z",
  "application": {
    "name": "gamify-hc",
    "version": "1.0.0",
    "environment": "production"
  },
  "uptime_seconds": 3600,
  "database": {
    "status": "ok",
    "type": "postgresql",
    "version": "PostgreSQL 16.1",
    "response_time_ms": 5
  }
}
```

**Use cases:**
- Monitoring dashboards (Datadog, New Relic, Grafana)
- Deployment verification
- Health status alerts

### `/api/health/live` - Liveness Probe

Checks if the application is running and responsive. Does NOT check database.

**Response (200 OK):**
```json
{
  "status": "ok",
  "probe": "liveness",
  "timestamp": "2025-12-11T10:30:45Z"
}
```

**Use cases:**
- Kubernetes liveness probe (restarts pod if fails)
- Basic uptime monitoring
- Process health verification

### `/api/health/ready` - Readiness Probe

Checks if the application can accept traffic. Includes database connectivity.

**Response (200 OK):**
```json
{
  "status": "ready",
  "probe": "readiness",
  "database": {
    "status": "ok",
    "type": "postgresql",
    "version": "PostgreSQL 16.1",
    "response_time_ms": 5
  },
  "timestamp": "2025-12-11T10:30:45Z"
}
```

**Response (503 Service Unavailable) - Not Ready:**
```json
{
  "status": "not_ready",
  "probe": "readiness",
  "reason": "database_unavailable",
  "database": {
    "status": "error",
    "error": "connection refused",
    "type": "postgresql"
  },
  "timestamp": "2025-12-11T10:30:45Z"
}
```

**Use cases:**
- Kubernetes readiness probe (removes from service if fails)
- Load balancer health checks
- Rolling deployment verification
- Database migration waiting

### Configuration Examples

**Kubernetes Probes:**
```yaml
livenessProbe:
  httpGet:
    path: /api/health/live
    port: 5001
  initialDelaySeconds: 30
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /api/health/ready
    port: 5001
  initialDelaySeconds: 10
  periodSeconds: 5
  timeoutSeconds: 3
  failureThreshold: 3
```

**Docker Compose Healthcheck:**
```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:5001/api/health/live"]
  interval: 30s
  timeout: 5s
  retries: 3
  start_period: 40s
```

**Load Balancer (nginx):**
```nginx
upstream backend {
  server backend1:5001;
  server backend2:5001;
}

location / {
  proxy_pass http://backend;
  
  # Health check configuration
  health_check interval=10s
               fails=3
               passes=2
               uri=/api/health/ready;
}
```

---

## Platform Deployment (Heroku/Railway)

The application includes a `Procfile` that defines process types for platform-as-a-service deployments.

### Process Types

#### `web` - HTTP Server
Runs the Gunicorn WSGI server with worker processes:
```
web: gunicorn --config backend/gunicorn_config.py run:app
```

**Scaling:**
```bash
# Heroku
heroku ps:scale web=2

# Railway
railway scale web --replicas 2
```

#### `release` - Pre-deployment Tasks
Runs before each deployment to seed the database:
```
release: python -m backend.cli seed
```

This ensures fresh deployments have initial course data.

### Heroku Deployment

1. **Create Heroku App:**
   ```bash
   heroku create gamify-hc
   ```

2. **Add PostgreSQL:**
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

3. **Set Environment Variables:**
   ```bash
   heroku config:set JWT_SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(32))")
   heroku config:set ENVIRONMENT=production
   heroku config:set LOG_FORMAT=json
   heroku config:set LOG_LEVEL=INFO
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

5. **Scale Workers (optional):**
   ```bash
   heroku ps:scale web=2
   ```

### Railway Deployment

1. **Create New Project:**
   ```bash
   railway init
   ```

2. **Add PostgreSQL:**
   ```bash
   railway add postgresql
   ```

3. **Set Environment Variables:**
   ```bash
   railway variables set JWT_SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(32))")
   railway variables set ENVIRONMENT=production
   railway variables set LOG_FORMAT=json
   ```

4. **Deploy:**
   ```bash
   railway up
   ```

---

## Container Deployment (Docker/Kubernetes)

### Docker Compose (Development)

Run all services with Docker Compose:

```bash
docker compose up --build
```

This starts:
- **PostgreSQL** on port 5432
- **Backend API** on port 5001
- **Frontend** on port 3000

### Docker Compose (Production)

Create `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: gamify_hc
      POSTGRES_USER: gamify
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: always

  backend:
    build:
      context: .
      dockerfile: backend/Dockerfile
    environment:
      DATABASE_URL: postgresql://gamify:${POSTGRES_PASSWORD}@postgres:5432/gamify_hc
      JWT_SECRET_KEY: ${JWT_SECRET_KEY}
      ENVIRONMENT: production
      LOG_FORMAT: json
      LOG_LEVEL: INFO
      GUNICORN_WORKERS: 4
    depends_on:
      - postgres
    restart: always
    ports:
      - "5001:5001"

  frontend:
    build:
      context: frontend
      dockerfile: Dockerfile
    depends_on:
      - backend
    restart: always
    ports:
      - "80:80"

volumes:
  postgres_data:
```

Deploy:
```bash
docker compose -f docker-compose.prod.yml up -d
```

### Kubernetes Deployment

Example Kubernetes manifests:

**backend-deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gamify-hc-backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: gamify-hc-backend
  template:
    metadata:
      labels:
        app: gamify-hc-backend
    spec:
      containers:
      - name: backend
        image: gamify-hc-backend:latest
        ports:
        - containerPort: 5001
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: gamify-secrets
              key: database-url
        - name: JWT_SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: gamify-secrets
              key: jwt-secret
        - name: ENVIRONMENT
          value: "production"
        - name: LOG_FORMAT
          value: "json"
        - name: GUNICORN_WORKERS
          value: "4"
        livenessProbe:
          httpGet:
            path: /api/health/live
            port: 5001
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /api/health/ready
            port: 5001
          initialDelaySeconds: 10
          periodSeconds: 5
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

---

## Scaling Strategy

### Horizontal Scaling

The application is designed to scale horizontally (add more instances):

**Backend:**
- ✅ **Stateless processes** - No server-side sessions
- ✅ **Database connection pooling** - Handles concurrent connections
- ✅ **Graceful shutdown** - Safe to terminate instances
- ✅ **Load balancer ready** - Any instance can handle any request

**Scaling Examples:**
```bash
# Heroku
heroku ps:scale web=4

# Kubernetes
kubectl scale deployment gamify-hc-backend --replicas=5

# Docker Compose
docker compose up --scale backend=3
```

### Vertical Scaling

Adjust worker processes and threads based on resources:

**CPU-bound workloads:**
```bash
GUNICORN_WORKERS=8        # 2 x CPU cores + 1
GUNICORN_THREADS=1        # Fewer threads for CPU work
GUNICORN_WORKER_CLASS=sync
```

**I/O-bound workloads:**
```bash
GUNICORN_WORKERS=4
GUNICORN_THREADS=4        # More threads for I/O wait
GUNICORN_WORKER_CLASS=gevent  # Use async workers
```

### Monitoring & Autoscaling

**Key Metrics to Monitor:**
- Response time (p50, p95, p99)
- Request rate (requests/second)
- Error rate (4xx, 5xx responses)
- Worker utilization
- Database connection pool usage

**Autoscaling Rules (Kubernetes HPA):**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: gamify-hc-backend-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: gamify-hc-backend
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

---

## Environment Configuration

### Required Environment Variables

All deployments require these variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host:5432/db` |
| `JWT_SECRET_KEY` | Secret for JWT signing | Generate with `secrets.token_urlsafe(32)` |
| `ENVIRONMENT` | Environment name | `production`, `staging`, `development` |

### Recommended Production Settings

```bash
# Security
JWT_SECRET_KEY=<strong-random-secret>
JWT_EXPIRATION_HOURS=24

# Logging
LOG_FORMAT=json
LOG_LEVEL=INFO

# Server
GUNICORN_WORKERS=4
GUNICORN_THREADS=2
GUNICORN_TIMEOUT=30
GUNICORN_GRACEFUL_TIMEOUT=30

# CORS
CORS_ORIGINS=https://yourdomain.com

# Database
SQLALCHEMY_ECHO=false
```

### Development vs Production

**Development (.env):**
```bash
ENVIRONMENT=development
LOG_FORMAT=text
LOG_LEVEL=DEBUG
DEBUG=true
SQLALCHEMY_ECHO=true
CORS_ORIGINS=*
```

**Production:**
```bash
ENVIRONMENT=production
LOG_FORMAT=json
LOG_LEVEL=INFO
DEBUG=false
SQLALCHEMY_ECHO=false
CORS_ORIGINS=https://app.example.com
```

---

## Pre-Deployment Checklist

- [ ] Set strong `JWT_SECRET_KEY` (not dev key)
- [ ] Configure production `DATABASE_URL`
- [ ] Set `ENVIRONMENT=production`
- [ ] Enable JSON logging (`LOG_FORMAT=json`)
- [ ] Configure CORS origins (not `*`)
- [ ] Disable debug mode (`DEBUG=false`)
- [ ] Set appropriate worker count (`GUNICORN_WORKERS`)
- [ ] Configure health check endpoints
- [ ] Set up monitoring/alerting
- [ ] Test database migrations/seeding
- [ ] Verify graceful shutdown works
- [ ] Load test with expected traffic

---

## Troubleshooting

### Database Connection Issues

**Problem:** `ValueError: DATABASE_URL environment variable is required`

**Solution:**
```bash
# Check if variable is set
echo $DATABASE_URL

# Set it if missing
export DATABASE_URL="postgresql://user:pass@host:5432/db"
```

### Worker Timeout Issues

**Problem:** Workers timing out under load

**Solution:**
```bash
# Increase timeout
GUNICORN_TIMEOUT=60
GUNICORN_GRACEFUL_TIMEOUT=60
```

### High Memory Usage

**Problem:** Workers consuming too much memory

**Solution:**
```bash
# Enable worker restart after N requests
GUNICORN_MAX_REQUESTS=1000
GUNICORN_MAX_REQUESTS_JITTER=50
```

### Slow Database Queries

**Problem:** Database connection pool exhausted

**Solution:** Increase pool size in `backend/database/setup.py`:
```python
engine = create_engine(
    database_url,
    pool_size=20,      # Increase from 10
    max_overflow=40,   # Increase from 20
)
```

---

## Additional Resources

- [12-Factor App Methodology](https://12factor.net/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [PostgreSQL Connection Pooling](https://www.postgresql.org/docs/current/pgpool.html)
- [Heroku Scaling Documentation](https://devcenter.heroku.com/articles/scaling)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
