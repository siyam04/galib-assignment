from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Increased length for hashed password
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
