from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields if needed
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)