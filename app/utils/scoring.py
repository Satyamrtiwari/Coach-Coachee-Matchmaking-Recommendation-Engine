from typing import List, Dict, Tuple
from app.models.schemas import Coach, Coachee, MatchResult, MatchExplanation

def calculate_match(coachee: Coachee, coach: Coach, similarity_score: float) -> Tuple[float, MatchExplanation]:
    """
    Calculates final match score based on composite criteria.
    Score out of 100% (represented as 0.0 to 1.0 internally, then scaled to 100).
    """
    score = 0.0
    
    # 1. Mandatory / High Weight: Language (30%)
    language_match = coachee.language in coach.languages
    if language_match:
        score += 0.30

    # 2. Text Similarity for Goals & Expertise (40%)
    score += similarity_score * 0.40

    # 3. Coaching Style (20%)
    style_match = coachee.preferred_coaching_style == coach.coaching_style
    if style_match:
        score += 0.20

    # 4. Industry Match (5%)
    industry_match = coachee.industry in coach.industries_served
    if industry_match:
        score += 0.05

    # 5. Experience Bonus (max 5% for up to 25+ years)
    exp_score = min(coach.years_of_experience / 25.0, 1.0) * 0.05
    score += exp_score

    # Construct Explanation
    reasons = []
    if language_match:
        reasons.append(f"Speaks {coachee.language}")
    else:
        reasons.append(f"Does not speak {coachee.language} (Penalty)")
        
    if style_match:
        reasons.append("Matches preferred coaching style")
        
    if industry_match:
        reasons.append("Has experience in your industry")
        
    if similarity_score > 0.1:
        reasons.append("Strong alignment with your goals and development areas")

    explanation_text = ". ".join(reasons) + "."

    explanation = MatchExplanation(
        language_match=language_match,
        style_match=style_match,
        industry_match=industry_match,
        expertise_similarity=round(similarity_score, 2),
        summary=explanation_text
    )

    return round(score * 100, 2), explanation
