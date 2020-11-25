from django.db import models
from django.utils import timezone

# Create your models here.
class UserAccount(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_lenght=255)
    lastUpdated = models.DateTimeField()
 
class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventDate = models.DateTimeField()
<<<<<<< HEAD
    eventDescription = models.CharField(max_length=255)
    hostedBy = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="host user")
=======
    eventDescription = models.CharField(max_lenght=255)
    hostedBy =  models.ForeignKey(UserAccount, on_delete=models.CASCADE)

>>>>>>> 9b6428fe7c70b0bd64998d4ffbb14fc5e243ca88
