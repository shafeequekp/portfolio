import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from core.models import Profile, Project

def update_media():
    # Update Profile
    profile = Profile.objects.first()
    if profile:
        profile.profile_image = 'profile/profile.png'
        profile.save()
        print("Updated Profile image.")
    else:
        print("No Profile found to update.")

    # Update Projects
    projects = Project.objects.all()
    if projects.exists():
        # Cycle through available project images
        images = ['projects/project1.png', 'projects/project2.png']
        for i, project in enumerate(projects):
            project.image = images[i % len(images)]
            project.save()
            print(f"Updated Project: {project.title}")
    else:
        print("No Projects found to update.")

if __name__ == "__main__":
    update_media()
