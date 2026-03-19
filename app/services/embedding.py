from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict
from app.models.schemas import Coach, Coachee

class EmbeddingService:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.coach_matrix = None
        self.coach_ids = []

    def _get_coach_text(self, coach: Coach) -> str:        # Combine reliviant text fields for embedding
        parts = coach.expertise_areas + coach.industries_served + coach.certifications
        return " ".join(parts)

    def _get_coachee_text(self, coachee: Coachee) -> str:
        parts = coachee.goals + coachee.development_areas + [coachee.industry]
        return " ".join(parts)

    def fit(self, coaches: List[Coach]):
        if not coaches:
            return
        
        self.coach_ids = [c.id for c in coaches]
        corpus = [self._get_coach_text(c) for c in coaches]
        self.coach_matrix = self.vectorizer.fit_transform(corpus)

    def get_similarities(self, coachee: Coachee) -> Dict[str, float]:
        if self.coach_matrix is None or not self.coach_ids:
            return {}
            
        coachee_text = self._get_coachee_text(coachee)
        coachee_vec = self.vectorizer.transform([coachee_text])    # Calcuulate cosine similarity between coachee and all coaches
        
        similarities = cosine_similarity(coachee_vec, self.coach_matrix).flatten()
        
        return {coach_id: float(score) for coach_id, score in zip(self.coach_ids, similarities)}

embedding_service = EmbeddingService()
