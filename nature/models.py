from django.db import models
from datetime import datetime 
# Create your models here.
class NaturePost(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title
    
    def approve(self):
        self.approved = True
        self.save()
    

