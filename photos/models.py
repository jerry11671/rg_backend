from django.db import models
from accounts.models import CustomUser

class Photo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='./pictures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username