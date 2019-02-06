from django.db import models

# Create your models here.

class BusinessPost(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.title