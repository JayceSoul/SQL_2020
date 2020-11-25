from django.db import models
from django.utils import timezone

# Create your models here.
class UserAccount(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_lenght=255)
    lastUpdated = models.DateTimeField()
 