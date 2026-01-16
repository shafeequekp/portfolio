import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from core.models import Profile, Skill, Experience

def populate():
    # 1. Create/Update Profile
    profile, created = Profile.objects.get_or_create(id=1)
    profile.name = "Muhammed Shafeek"
    profile.title = "Python Developer"
    profile.bio = "Python Developer at Classyserver Technologies, Kochi. Specializing in building scalable applications, microservices, and ETL pipelines."
    profile.email = "shafeek@example.com" # Placeholder as email wasn't explicitly given for contact
    profile.linkedin_link = "https://www.linkedin.com/in/shafeek-kp/"
    profile.github_link = "https://github.com/shafeequekp"
    profile.profile_image = "profile/profile.jpg"
    profile.save()
    print(f"Profile updated: {profile.name}")

    # 2. Add Experience
    Experience.objects.all().delete() # Clear existing to avoid dupes
    Experience.objects.create(
        role="Python Developer",
        company="Classyserver Technologies",
        start_date=date(2022, 1, 1), # Approx date
        is_current=True,
        description="Working on scalable applications, backend development with Django/FastAPI, and cloud infrastructure on AWS. Address: Aminas, Kottanicher, Kanhirode PO, 670592 PIN."
    )
    print("Experience added.")

    # 3. Add Skills
    Skill.objects.all().delete()
    
    skills_data = [
        # Backend
        ("Python", 90, "fab fa-python", "Backend"),
        ("Django", 90, "fas fa-code", "Backend"),
        ("Django REST Framework", 85, "fas fa-cogs", "Backend"),
        ("FastAPI", 80, "fas fa-bolt", "Backend"),
        ("Java Basics", 60, "fab fa-java", "Backend"),
        ("Pandas", 75, "fas fa-table", "Backend"),
        ("Celery", 70, "fas fa-tasks", "Backend"),
        ("Redis", 70, "fas fa-database", "Backend"),
        
        # Database & Infra
        ("Postgres", 85, "fas fa-database", "Backend"),
        ("AWS", 70, "fab fa-aws", "Tools"),
        ("Docker", 75, "fab fa-docker", "Tools"),
        ("CI/CD", 70, "fas fa-sync", "Tools"),
        ("Nginx/Apache", 65, "fas fa-server", "Tools"),
        ("Linux", 80, "fab fa-linux", "Tools"),
        
        # Concepts
        ("Microservices", 75, "fas fa-network-wired", "Technical"),
        ("ETL", 70, "fas fa-stream", "Technical"),
        ("DSA", 70, "fas fa-brain", "Technical"),
        ("Debugging/Logging", 85, "fas fa-bug", "Technical"),
        ("QA", 65, "fas fa-vial", "Technical"),
        
        # Frontend
        ("HTML5", 95, "fab fa-html5", "Frontend"),
        ("CSS3", 85, "fab fa-css3-alt", "Frontend"),
        ("JavaScript", 80, "fab fa-js", "Frontend"),
        ("Bootstrap", 85, "fab fa-bootstrap", "Frontend"),
        ("React", 65, "fab fa-react", "Frontend"),
    ]

    for name, prof, icon, cat in skills_data:
        Skill.objects.create(
            name=name,
            proficiency=prof,
            icon_class=icon,
            category=cat
        )
    print(f"Added {len(skills_data)} skills.")

if __name__ == '__main__':
    populate()
