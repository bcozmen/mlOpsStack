from django.shortcuts import render

def home(request):
    # We can pass portfolio project metadata directly to the template dynamically
    portfolio_projects = [
        {
            "title": "🏡 Real Estate ML Valuation Engine",
            "description": "A containerized Scikit-Learn pipeline deployed via FastAPI with live database performance logging.",
            "url_name": "mlops", # This will match our URL pattern name later,
            "tags": ["Python", "MLOps", "Architecture"] # Example tags for visual display
        },
        {
            "title": "🏡 Real Estate ML Valuation Engine",
            "description": "A containerized Scikit-Learn pipeline deployed via FastAPI with live database performance logging.",
            "url_name": "mlops" # This will match our URL pattern name later
        },
        {
            "title": "🏡 Real Estate ML Valuation Engine",
            "description": "A containerized Scikit-Learn pipeline deployed via FastAPI with live database performance logging.",
            "url_name": "mlops" # This will match our URL pattern name later
        },
        {
            "title": "🏡 Real Estate ML Valuation Engine",
            "description": "A containerized Scikit-Learn pipeline deployed via FastAPI with live database performance logging.",
            "url_name": "mlops" # This will match our URL pattern name later
        },
        {
            "title": "🏡 Real Estate ML Valuation Engine",
            "description": "A containerized Scikit-Learn pipeline deployed via FastAPI with live database performance logging.",
            "url_name": "mlops" # This will match our URL pattern name later
        },
        {
            "title": "🏡 Real Estate ML Valuation Engine",
            "description": "A containerized Scikit-Learn pipeline deployed via FastAPI with live database performance logging.",
            "url_name": "mlops" # This will match our URL pattern name later
        },
    ]
    
    context = {
        "projects": portfolio_projects
    }
    return render(request, 'frontend/home.html', context)

def mlops(request):
    # Pass the FastAPI URL to the template so JS knows where to send requests
    context = {
        'fastapi_url': 'http://127.0.0.1:8002'
    }
    return render(request, 'frontend/spatial_dashboard.html', context)