from fastapi import APIRouter
from app.models.schemas import Coachee, MatchResponse
from app.services.matcher import matcher_service

router = APIRouter()

@router.post("/match", response_model=MatchResponse)
async def match_coach(coachee: Coachee):
    """
    Accepts a Coachee profile and returns the top 5 recommended coaches.
    Matches using a hybrid of rule-based logic and TF-IDF similarity.
    """
    top_matches = matcher_service.find_top_matches(coachee, top_k=5)
    return MatchResponse(coachee_name=coachee.name, top_matches=top_matches)
