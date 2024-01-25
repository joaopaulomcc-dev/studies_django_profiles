from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    text = models.TextField()

    def __str__(self):
        summary = self.text[:50] if len(self.text) >= 50 else self.text
        return summary
