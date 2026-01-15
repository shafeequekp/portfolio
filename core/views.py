from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, Service, Testimonial, ContactMessage

def index(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'services': services,
        'testimonials': testimonials,
    }
    return render(request, 'core/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')
    return redirect('index')
