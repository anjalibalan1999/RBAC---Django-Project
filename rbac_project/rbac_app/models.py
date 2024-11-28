from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        (0, "Admin"),
        (1, "Moderator"),
        (2, "User"),
    )
    role = models.IntegerField(choices=ROLE_CHOICES, default=2)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.user.username}"
