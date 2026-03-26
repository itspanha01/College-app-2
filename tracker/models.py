from django.db import models
from django.contrib.auth.models import User

class College(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    acceptance_rate = models.FloatField(null=True, blank=True)
    tuition = models.IntegerField(null=True, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
class Application(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('submitted', 'Submitted'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')

    def __str__(self):
        return f"{self.user.username} → {self.college.name}"