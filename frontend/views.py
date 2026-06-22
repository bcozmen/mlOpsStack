import os
from django.shortcuts import render

def home(request):
    # We can pass portfolio project metadata directly to the template dynamically
    portfolio_projects = [
        {
            "title": "ML Pipeline with FastAPI",
            "description": "A containerized Scikit and pytorch ML pipeline with FastAPI for model serving and Database models for tracking experiments.",
            "url_name": "mlops", # This will match our URL pattern name later,
            "tags": ["Python", "MLOps", "Architecture"] # Example tags for visual display
        },
    ]
    
    context = {
        "projects": portfolio_projects
    }
    return render(request, 'frontend/home.html', context)

def mlops(request):
    # Use environment variable on VPS, fallback to localhost for dev
    # On VPS, set FASTAPI_URL="https://portfolio.zettelweb.com/api" (or your specific API port)
    default_url = f"{request.scheme}://{request.get_host().split(':')[0]}:8002"
    fastapi_url = os.environ.get('FASTAPI_URL', default_url)
    
    context = {
        'fastapi_url': https://portfolio.zettelweb.com/api # Replace with your actual domain
    }
    return render(request, 'frontend/spatial_dashboard.html', context)