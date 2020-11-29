from django.db import models
from django.utils import timezone




# Create your models here.
class UserAccount(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=255)
    lastUpdated = models.DateTimeField()
    def __str__(self):
        return self.username

class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    eventDate = models.DateTimeField()
    eventDescription = models.CharField(max_length=255)
    hostedby = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Sighting(models.Model):
    sightID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=63)
    notes = models.CharField(max_length=255)
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
    content = models.CharField(max_length=255)
    postTime = models.DateTimeField()
    createdBy = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    onSighting = models.ForeignKey(Sighting,on_delete=models.CASCADE)

class Attends(models.Model):
    eventId = models.ForeignKey(Event,on_delete=models.CASCADE)
    personId = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    def __str__(self):
        return self.personId.username + " -> " + self.eventId.title


class Animal(models.Model):
    animalId = models.AutoField(primary_key=True)
    diet =  models.CharField(max_length=255)
    name =  models.CharField(max_length=255)
    description =  models.CharField(max_length=255)
    animalType  =  models.CharField(max_length=255)
    def __str__(self):
        return  self.name

class Plant(models.Model):
    plantId = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255)
    scientificName =  models.CharField(max_length=255)
    averageHeight = models.IntegerField()#size 8
    plantDescription =  models.CharField(max_length=255)
    fruitBearing = models.IntegerField()# size 1
    lightRequirement =  models.CharField(max_length=255)
    waterRequirement = models.CharField(max_length=255)
    leafType = models.CharField(max_length=255)
    plantType = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class AnimalSighting(models.Model):
    sightId = models.ForeignKey(Sighting,on_delete=models.CASCADE)
    seasonalBehavior =  models.CharField(max_length=255)
    health = models.CharField(max_length=255)
    herdSize = models.IntegerField()
    animalType = models.ForeignKey(Animal,on_delete=models.CASCADE)

class PlantSighting(models.Model):
    sightId = models.AutoField(primary_key=True)
    soil =  models.CharField(max_length=255)
    height = models.IntegerField()#size 16
    health =  models.CharField(max_length=25)
    flowering = models.IntegerField()# size 1
    plantType = models.ForeignKey(Plant,on_delete=models.CASCADE)

class ConsumeAnimal(models.Model):
    consumer = models.ForeignKey(Animal,on_delete=models.CASCADE, related_name = 'consumer')
    consumed = models.ForeignKey(Animal,on_delete=models.CASCADE, related_name = 'consumed')
    def __str__(self):
        return self.consumer.name + " -> " + self.consumed.name


class ConsumePlant(models.Model):
    Animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    Plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Animal) + " -> " + str(self.Plant)

class Location(models.Model):
    locationId = models.AutoField(primary_key=True)
    climate = models.CharField(max_length=255)
    commonName = models.CharField(max_length=255)
    latLoc = models.IntegerField()
    LongLoc = models.IntegerField()

class Flag(models.Model):
    flagId =  models.ForeignKey(Sighting,on_delete=models.CASCADE)
    colour = models.CharField(max_length=6)
    dangerLevel = models.IntegerField()
    latLoc =  models.IntegerField()
    LongLoc = models.IntegerField()
    type = 	models.IntegerField()#size 1 also need to change name
    referenceType = models.IntegerField()

class Lives(models.Model):
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)