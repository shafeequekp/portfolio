import os
import django
import requests

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from core.models import Project

GITHUB_USERNAME = "shafeequekp"
API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?sort=updated&per_page=6"

def fetch_projects():
    print(f"Fetching projects for user: {GITHUB_USERNAME}...")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        repos = response.json()
        
        count = 0
        for repo in repos:
            # Skip forked repos if desired, but user said "my github account" so user might want forks too.
            # Let's include everything but prioritize non-forks if we were sorting manually.
            # GitHub API 'sort=updated' gives most recently active.
            
            project, created = Project.objects.update_or_create(
                title=repo['name'],
                defaults={
                    'description': repo['description'] or "No description provided.",
                    'technologies': repo['language'] or "Various",
                    'github_link': repo['html_url'],
                    'demo_link': repo['homepage'] if repo['homepage'] else "",
                    # We don't have an image from API easily without scraping OpenGraph, 
                    # so we will rely on the template's "No Image" placeholder or manually update later.
                }
            )
            action = "Created" if created else "Updated"
            print(f"[{action}] {project.title}")
            count += 1
            
        print(f"Successfully processed {count} projects.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub: {e}")

if __name__ == "__main__":
    fetch_projects()
