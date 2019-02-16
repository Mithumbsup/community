from django.db import models

# Create your models here.
class EngineerPost(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def approve(self):
        self.approved = True
        self.save()
