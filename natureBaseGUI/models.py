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
    eventDescription = models.CharField(max_lenght=255)
    hostedBy =  models.ForeignKey(UserAccount, on_delete=models.CASCADE)









class Animal(modles.Model):
    animalId = models.AutoField(primary_key=True)
    diet =  models.CharField(max_lenght=255)
    name =  models.CharField(max_lenght=255)
    description =  models.CharField(max_lenght=255)
    animalType  =  models.CharField(max_lenght=255)

class Plant(models.Model):
    plantId = models.AutoField(primary_key=True)
    name =  models.CharField(max_lenght=255)
    scientificName =  models.CharField(max_lenght=255)
    averageHeight = models.IntegerField()#size 8
    plantDescription =  models.CharField(max_lenght=255)
    fruitBearing = models.IntegerField()# size 1
    lightRequirement =  models.CharField(max_lenght=255)
    waterRequirement = models.CharField(max_lenght=255)
    leafType = models.CharField(max_lenght=255)
    plantType = models.CharField(max_lenght=255)

class AnimalSighting(models.Model):
    sightId = models.ForeignKey(Sighting)
    seasonalBehavior =  models.CharField(max_lenght=255)
    health = models.CharField(max_lenght=255)
    herdSize = models.IntegerField()
    animalType = models.ForeignKey(Animal)


class PlantSighting(models.Model):
    sightId = models.AutoField(primary_key=True)
    soil =  models.CharField(max_lenght=255)
    height = models.IntegerField()#size 16
    health =  models.CharField(max_lenght=25)
    flowering = models.IntegerField()# size 1
    plantType = models.ForeignKey(Plant)

class ConsumeAnimal(models.Model):
    consumer = models.ForeignKey(Animal)
    consumed = models.ForeignKey(Animal)

class ConsumePlant(models.Model):
    Animal = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    Plant = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

class Location(models.Model):
    locationId = models.AutoField(primary_key=True)
    climate = models.CharField(max_lenght=255)
    commonName = models.CharField(max_lenght=255)
    latLoc = models.IntegerField()
    LongLoc = 	models.IntegerField()

class Flag(models.Model):
    flagId =  models.ForeignKey(Sighting)
    colour = models.CharField(max_lenght=6)
    dangerLevel = models.IntegerField()
    latLoc =  models.IntegerField()
    LongLoc = models.IntegerField()
    type = 	models.IntegerField()#size 1 also need to change name
    referenceType = models.IntegerField()

class Lives(models.Model):
    plant = models.ForeignKey(Plant)
    animal = models.ForeignKey(Animal)
    location = models.ForeignKey(Location)

    