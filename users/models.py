from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    
    created = models.DateTimeField(
        auto_now_add = True, 
        verbose_name="Creation date"
    )

    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="Update date"
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("created", )
