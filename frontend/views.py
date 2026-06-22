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
    # Detect the environment:
    host = request.get_host().split(':')[0]
    
    if host in ['localhost', '127.0.0.1']:
        default_url = "http://127.0.0.1:8002"
    else:
        # Request via Nginx, so use the /api proxy
        default_url = f"https://{host}/api"
        
    fastapi_url = os.environ.get('FASTAPI_URL', default_url)
    
    context = {
        'fastapi_url': fastapi_url
    }
    return render(request, 'frontend/spatial_dashboard.html', context)