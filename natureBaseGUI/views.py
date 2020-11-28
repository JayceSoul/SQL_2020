from django.shortcuts import render
from django.http import HttpResponse

from .models import Animal, Plant, UserAccount, Event, Attends
from .links import PLANT_PICTURE,ANIMAL_PICTURE,PLACEHOLD_PICTURE
# Create your views here.


def index(request):
    html = '<html><body> potato <body></html>'
    return HttpResponse(html)


def pathing(request,input_id):
    return HttpResponse("tester %s " % input_id)


def showAllAnimals(request):
    context = {
        'entity_list': Animal.objects.all(),
        'entity_name':'Animals',
    }
    return render(request, 'listAnimals.html', context)

def showAllPlants(request):
    context = {
        'entity_list': Plant.objects.all(),
        'entity_name':'Plants',
    }
    return render(request, 'listPlants.html', context)

def showPlant(request,plant_id):
    plant = Plant.objects.get(pk=plant_id)
    attrToDisplay = ('name','scientificName','plantDescription')
    attrValuePair = []
    for atr in attrToDisplay:
        attrValuePair.append( (atr,getattr(plant,atr)) )
    context = {
        'name': plant.name,
        'entity_type': 'plant',
        'attributes': attrValuePair,
        'active': attrToDisplay[0],
        'picture': PLANT_PICTURE,
    }
    return render(request, 'entity.html', context)

def showAnimal(request,animal_id):
    animal = Animal.objects.get(pk=animal_id)
    attrToDisplay = ('name','diet','description')
    attrValuePair = []
    for atr in attrToDisplay:
        attrValuePair.append( (atr,getattr(animal,atr)) )
    context = {
        'name': animal.name,
        'entity_type': 'animal',
        'attributes': attrValuePair,
        'active': attrToDisplay[0],
        'picture': ANIMAL_PICTURE,
    }
    return render(request, 'entity.html', context)

def showUser(request,user_id):
    user = UserAccount.objects.get(pk=user_id)
    attrToDisplay = ('username','lastUpdated')
    attrValuePair = []
    for atr in attrToDisplay:
        attrValuePair.append( (atr,getattr(user,atr)) )
    context = {
        'name': user.username,
        'entity_type': 'user',
        'attributes': attrValuePair,
        'active': attrToDisplay[0],
        'picture': PLACEHOLD_PICTURE,
    }
    return render(request, 'entity.html', context)

def showAllEvents(request):
    events = Event.objects.all()
    displayInfo = []
    for event in events:
        eventId = event.eventId
        attendees = Attends.objects.filter(eventId = eventId)
        personAttendees = [x.personId for x in attendees]
        print("attendees for " + str(eventId))
        print(personAttendees)
        displayInfo.append( (event,personAttendees) )
    
    context = {
        'events': displayInfo,
    }
    return render(request, 'event.html', context)

def devGround(request):
    context = {
        'entity_list': Animal.objects.all(),
        'entity_name': Animal._meta.fields,
        'attrs':['name'],
    }
    return render(request, 'testGround.html',context)

