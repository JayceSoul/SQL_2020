from django.db import models
from django.utils import timezone

# Create your models here.
class UserAccount(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=255)
    lastUpdated = models.DateTimeField()
 
class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventDate = models.DateTimeField()
    eventDescription = models.CharField(max_lenght=255)
    hostedby = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

class Sighting(models.Model):
    sightID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=63)
    notes = models.CharField(max_length=500)
    latloc = models.FloatField()
    longloc = models.FloatField()
    lastUpdated = models.DateTimeField()
    timeRecorded = models.DateTimeField()
    sightedBy = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    partOfEvent = models.ForeignKey(Event,on_delete=models.CASCADE)

class UserSightingSaved(models.Model):
    sightSaved = models.AutoField(primary_key=True)
    savedBy = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    sightingId = models.ForeignKey(Sighting,on_delete=models.CASCADE)

class SightingComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    content = models.CharField(2047)
    postTime = models.DateTimeField()
    createdBy = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    onSighting = models.ForeignKey(Sighting,on_delete=models.CASCADE)

class Attends(models.Model):
    eventId = models.ForeignKey(Event,on_delete=models.CASCADE)
    personId = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
   
