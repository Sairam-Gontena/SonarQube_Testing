from fastapi import FastAPI

from controllers.routes import all_routes
from config import app_config

app = FastAPI(
    title=app_config.PROJECT_NAME,
    version=app_config.VERSION,
)

# Include all routes in controllers included in routes.py
app.include_router(all_routes)

@app.get("/")
def root_greeting():
    """Greeting Message API"""
    return {"message": "Welcome to Constance python questionnaire api"}
