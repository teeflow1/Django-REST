from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=50)
    website = models.URLField(max_length=20)
    
    def __str__(self):
        return self.name
    
    verbose_name_plural = 'Account'
    
    
class Cinema(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    movie = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="movies")
    created_at = models.DateTimeField(auto_now_add=True)