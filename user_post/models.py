from django.db import models
from django.conf import settings
from datetime import datetime, date
from django.db.models.deletion import CASCADE


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True, auto_now=False, blank =True )
    updated_at=models.DateTimeField(auto_now_add=False, auto_now=True, blank =True)

    

    def __str__(self):
        return self.text