import json
from typing import List
from app.models.schemas import Coach
from app.core.config import settings

class Database:
    def __init__(self):
        self.coaches: List[Coach] = []

    def load_data(self):
        try:
            with open(settings.DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.coaches = [Coach(**c) for c in data]
        except FileNotFoundError:
            print(f"Data file not found at {settings.DATA_FILE}. Starting with empty database.")
            self.coaches = []

    def get_all_coaches(self) -> List[Coach]:
        return self.coaches

db = Database()
