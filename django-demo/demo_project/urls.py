import os
import platform

from django.http import HttpResponse, JsonResponse
from django.urls import path


def health_check(request):
    """Health check endpoint used by CloudNest to verify container readiness."""
    return JsonResponse({
        "status": "healthy",
        "service": "cloudnest-django-demo",
        "app_slug": os.getenv("CLOUDNEST_APP", "demo"),
        "deployment_id": os.getenv("CLOUDNEST_DEPLOYMENT", "local"),
    })

def home(request):
    """Simple welcoming status page."""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CloudNest Demo App</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-950 text-slate-100 flex items-center justify-center min-h-screen p-4 font-sans">
        <div class="max-w-md w-full bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-2xl text-center">
            <div class="w-14 h-14 bg-indigo-600/20 text-indigo-400 border border-indigo-500/40 rounded-2xl flex items-center justify-center mx-auto mb-5 text-2xl font-bold">
                🚀
            </div>
            <h1 class="text-2xl font-bold text-white tracking-tight">Django App Deployed!</h1>
            <p class="text-xs text-slate-400 mt-2">
                Running seamlessly on <strong class="text-indigo-400">CloudNest PaaS</strong> without manual server configuration.
            </p>
            <div class="mt-6 pt-6 border-t border-slate-800 text-left text-xs font-mono space-y-2 text-slate-300">
                <div class="flex justify-between">
                    <span class="text-slate-500">Service:</span>
                    <span>{os.getenv("CLOUDNEST_APP", "django-demo")}</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-slate-500">Health Endpoint:</span>
                    <a href="/healthz" class="text-indigo-400 hover:underline">/healthz</a>
                </div>
                <div class="flex justify-between">
                    <span class="text-slate-500">Python:</span>
                    <span>{platform.python_version()}</span>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path("", home, name="home"),
    path("healthz", health_check, name="healthz"),
]
