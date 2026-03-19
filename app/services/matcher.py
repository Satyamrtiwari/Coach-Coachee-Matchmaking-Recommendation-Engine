from typing import List
from app.models.schemas import Coachee, MatchResult
from app.models.database import db
from app.services.embedding import embedding_service
from app.utils.scoring import calculate_match

class MatcherService:
    def __init__(self):
        # We assume the database is already loaded when this is initialized, or we load it here.
        # In a real app we'd want to handle updates to the coach list nicely.
        pass

    def initialize(self):
        coaches = db.get_all_coaches()
        embedding_service.fit(coaches)

    def find_top_matches(self, coachee: Coachee, top_k: int = 5) -> List[MatchResult]:
        coaches = db.get_all_coaches()
        if not coaches:
            return []

        similarities = embedding_service.get_similarities(coachee)
        
        results = []
        for coach in coaches:
            sim_score = similarities.get(coach.id, 0.0)
            final_score, explanation = calculate_match(coachee, coach, sim_score)
            
        
            # but for soft ranking we just include them.
            
            result = MatchResult(
                coach=coach,
                match_score=final_score,
                explanation=explanation
            )
            results.append(result)
            
        # Sort by match score descending
        results.sort(key=lambda x: x.match_score, reverse=True)
        
        return results[:top_k]

matcher_service = MatcherService()
