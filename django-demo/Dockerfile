# Multi-stage / lightweight Python base image
FROM python:3.12-slim

# Enforce security best practice: run container as non-root user
RUN groupadd -r -g 1000 appuser && \
    useradd -r -u 1000 -g appuser -d /app -s /sbin/nologin appuser

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Assign ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to unprivileged user
USER appuser

EXPOSE 8000

# Production gunicorn entrypoint, binding to 0.0.0.0
CMD ["gunicorn", "demo_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "60", "--access-logfile", "-", "--error-logfile", "-"]
