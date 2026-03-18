import os

class Settings:
    PROJECT_NAME: str = "Coach-Coachee Matchmaking Recommendation Engine"
    API_V1_STR: str = "/api/v1"
    DATA_FILE: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "coaches.json")

settings = Settings()
