from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Peanut(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    image_url = models.URLField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    


