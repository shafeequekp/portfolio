from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, help_text="e.g. Full Stack Developer")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    resume = models.FileField(upload_to='docs/', blank=True, null=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text="Percentage 0-100")
    icon_class = models.CharField(max_length=50, help_text="FontAwesome or similar icon class")
    category = models.CharField(max_length=50, default='Technical', choices=[
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Tools', 'Tools'),
        ('Soft Skills', 'Soft Skills')
    ])

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    technologies = models.CharField(max_length=200, help_text="Comma separated list of techs")
    category = models.CharField(max_length=50, default='Web Dev')

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
