# Sample Django Application for CloudNest PaaS

This is a production-hardened demo Django application configured for deployment on CloudNest PaaS.

## Features
- **Non-Root Execution**: Runs under an unprivileged user `appuser:1000:1000`.
- **Health Check Endpoint**: Provides `/healthz` for deployment verification.
- **Dynamic Configuration**: Automatically binds to `$PORT` (default: 8000) and reads `$ALLOWED_HOSTS`.
- **Production WSGI**: Uses `gunicorn` with concurrency workers.

## How to Deploy on CloudNest
1. Push this repository or use an approved public GitHub repository.
2. In the CloudNest Dashboard, click **New Application**.
3. Fill in:
   - **Repository URL**: `https://github.com/<your-username>/<repo-name>`
   - **Git Branch**: `main`
   - **Internal Port**: `8000`
4. Click **Create Application**.
5. Click **Deploy**.
6. CloudNest will clone the repository, build the Docker container image, start the container with security sandboxing, verify the `/healthz` endpoint, and route requests to `http://<slug>.localhost`.
