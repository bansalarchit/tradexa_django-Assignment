from django.db import models
from django.conf import settings
from datetime import datetime, date
from django.db.models.deletion import CASCADE


class Product(models.Model):
    #user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1,null=True, on_delete=models.SET_NULL, db_constraint=False )

    name=models.CharField(max_length=100)
    weight=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True, auto_now=False )
    updated_at=models.DateTimeField(auto_now_add=False, auto_now=True)
    

    def __str__(self):
        return self.name
