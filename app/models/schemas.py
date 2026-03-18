from pydantic import BaseModel, Field
from typing import List

class Coach(BaseModel):
    id: str
    name: str
    expertise_areas: List[str]
    coaching_style: str
    industries_served: List[str]
    certifications: List[str]
    languages: List[str]
    years_of_experience: int

class Coachee(BaseModel):
    id: str = "coachee_1"
    name: str
    goals: List[str]
    industry: str
    role_level: str
    development_areas: List[str]
    preferred_coaching_style: str
    language: str

class MatchExplanation(BaseModel):
    language_match: bool
    style_match: bool
    industry_match: bool
    expertise_similarity: float
    summary: str

class MatchResult(BaseModel):
    coach: Coach
    match_score: float
    explanation: MatchExplanation

class MatchResponse(BaseModel):
    coachee_name: str
    top_matches: List[MatchResult]
