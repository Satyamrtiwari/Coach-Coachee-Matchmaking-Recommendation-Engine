import json
import random
import os

# Data pools for generating realistic profiles
first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]

expertise_pool = [
    "Leadership", "Executive Presence", "Public Speaking", "Career Transition", 
    "Agile Methodologies", "Team Building", "Conflict Resolution", "Negotiation", 
    "Startup Scaling", "Product Management", "Innovation", "Work-Life Balance", 
    "Stress Management", "Mindfulness", "Sales Leadership", "Business Development", 
    "Software Engineering Leadership", "System Design", "Diversity and Inclusion", 
    "HR Strategy", "Marketing Strategy", "Brand Building", "Board Relations"
]

styles = ["Directive", "Facilitative", "Transformational"]

industries_pool = [
    "Technology", "Finance", "Healthcare", "Retail", "Manufacturing", 
    "Startups", "Education", "Real Estate", "Media", "Non-Profit"
]

certifications_pool = ["ICF-ACC", "ICF-PCC", "ICF-MCC", "BCC", "NBHWC", "Scrum Master", "SHRM-CP", "CPA", "PMP"]

languages_pool = ["English", "Spanish", "French", "German", "Mandarin", "Hindi", "Arabic"]

def generate_coaches(num=100):
    coaches = []
    
    # Ensure English is dominant but others exist
    for i in range(1, num + 1):
        num_expertise = random.randint(2, 5)
        num_industries = random.randint(1, 3)
        num_certs = random.randint(0, 2)
        
        # 80% speak English, some speak multiple
        langs = ["English"] if random.random() < 0.8 else [random.choice(languages_pool)]
        if random.random() < 0.3:
            langs.append(random.choice([l for l in languages_pool if l not in langs]))
            
        coach = {
            "id": f"c{i}",
            "name": f"Coach {random.choice(first_names)} {random.choice(last_names)}",
            "expertise_areas": random.sample(expertise_pool, num_expertise),
            "coaching_style": random.choice(styles),
            "industries_served": random.sample(industries_pool, num_industries),
            "certifications": random.sample(certifications_pool, num_certs),
            "languages": langs,
            "years_of_experience": random.randint(3, 30)
        }
        coaches.append(coach)
        
    return coaches

if __name__ == "__main__":
    # Path to coaches.json
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, "coaches.json")
    
    coaches_data = generate_coaches(100)
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(coaches_data, f, indent=2)
        
    print(f"Successfully generated {len(coaches_data)} coaches in {file_path}")
