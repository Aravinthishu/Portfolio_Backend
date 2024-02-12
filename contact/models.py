from django.db import models

# Create your models here.

class ContactModels(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
