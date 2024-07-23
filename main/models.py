from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    reason = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"
    

