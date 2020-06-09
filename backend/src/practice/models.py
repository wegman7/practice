from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.user.username