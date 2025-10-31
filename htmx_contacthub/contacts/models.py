from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='contacts')

    class Meta:
        unique_together = ('user', 'email') # no two contacts can have the same email address for the same user

    def __str__(self):
        return f"{self.name} - {self.email}"