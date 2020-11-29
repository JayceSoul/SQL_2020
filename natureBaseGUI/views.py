from django.shortcuts import render
from django.http import HttpResponse

from .models import Animal, Plant, Sighting, Location, UserAccount, Event, Attends, UserSightingSaved, SightingComment, ConsumeAnimal, ConsumePlant
from .links import PLANT_PICTURE,ANIMAL_PICTURE,PLACEHOLD_PICTURE, EYE_PICTURE, PERSON_PICTURE
# Create your views here.


def index(request):
    html = '''
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
body {
  background-color: #a2d397;
}

div.navcontainer {
  background-color: #333;
  overflow: auto;
  white-space: nowrap;
}

div.navcontainer a {
  display: inline-block;
  color: white;
  text-align: center;
  padding-top: 14px;
  padding-bottom: 14px;
  padding-left: 150px;
  padding-right: 150px;
  text-decoration: none;
}

div.navcontainer a:hover {
  background-color: #777;
}
</style>
    </head>
    <body>
    <div class = "navcontainer">
            <a href="http://127.0.0.1:8000/animal">Animal</a>
            <a href="http://127.0.0.1:8000/plant">Plant</a>
            <a href="http://127.0.0.1:8000/location">Location</a>
    </div>
    </body>
    </html>
    '''
    return render(request, 'index.html', {} )
    #return HttpResponse(html)
    # <img src ="https://lh3.googleusercontent.com/proxy/NCOuz6-ERxED7wRti52DF1ROkj9BLnGTtye-F3NvwWO6_qgRjQYxkbnwdXbIm1TeMJtAr6pyNwtOcy5kPfkWriOTrB2WfweZQc-dDdlNpTrI92u-XdyVlqdiXWg_3JVJgGkfc53yQs-D0mdPt2QbSAep2gkhQJnS_8QPFvwejw" alt="leaves" class=overlay>


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

def showAllSightings(request):
    context = {
        'entity_list': Sighting.objects.all(),
        'entity_name':'Sightings',
    }
    return render(request, 'listSightings.html', context)

def showAllLocations(request):
    context = {
        'entity_list': Location.objects.all(),
        'entity_name':'Locations',
    }
    return render(request, 'listLocations.html', context)

def showAllUser(requets):
    context = {
        'entity_list': UserAccount.objects.all(),
        'entity_name':"Users",
    }
    return render(requets,'listUser.html',context)

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

def showSighting(request,sight_id):
    sighting = Sighting.objects.get(pk=sight_id)
    attrToDisplay = ('title', 'sightedBy', 'partOfEvent', 'latloc', 'longloc', 'notes', 'lastUpdated', 'timeRecorded')
    attrValuePair = []
    for atr in attrToDisplay:
        attrValuePair.append( (atr,getattr(sighting,atr)) )
    context = {
        'name': sighting.title,
        'entity_type': 'sighting',
        'attributes': attrValuePair,
        'active': attrToDisplay[0],
        'picture': EYE_PICTURE,
        'comments': SightingComment.objects.filter(onSighting=sight_id),
        'saved': UserSightingSaved.objects.filter(sightingId=sight_id),
    }
    return render(request, 'sighting.html', context)

def showLocation(request,sight_id):
    location = Location.objects.get(pk=location_id)
    attrToDisplay = ('commonName', 'climate', 'latLoc', 'longLoc')
    attrValuePair = []
    for atr in attrToDisplay:
        attrValuePair.append( (atr,getattr(location,atr)) )
    context = {
        'title': location.commonName,
        'entity_type': 'location',
        'attributes': attrValuePair,
        'active': attrToDisplay[0],
        'picture': PLACEHOLD_PICTURE,
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
        'picture': PERSON_PICTURE,
    }
    return render(request, 'entity.html', context)

def showAllEvents(request):
    events = Event.objects.all()
    displayInfo = []
    for event in events:
        eventId = event.eventId
        attendees = Attends.objects.filter(eventId = eventId)
        personAttendees = [x.personId for x in attendees]
        displayInfo.append( (event,personAttendees) )
    
    context = {
        'events': displayInfo,
    }
    return render(request, 'event.html', context)


def showAllFlags(request):
    context = {
        'entity_list': Flag.objects.all(),
        'entity_name':'Flags',
    }
    return render(request, 'listFlags.html', context)

def showConsumeAnimal(request):
    consumers = ConsumeAnimal.objects.all().values("consumer").distinct()
    displayInfo = []
    for con in consumers:
        consumed = ConsumeAnimal.objects.filter(consumer=con["consumer"])
        displayInfo.append( (Animal.objects.filter(pk=con["consumer"]).first(),consumed) )
    
    context = {
        'display': displayInfo,
    }
    return render(request, 'consumedAn.html', context)

def showConsumePlant(request):
    consumers = ConsumePlant.objects.all().values("Animal").distinct()
    displayInfo = []
    for con in consumers:
        consumed = ConsumePlant.objects.filter(Animal=con["Animal"])
        displayInfo.append( (Animal.objects.filter(pk=con["Animal"]).first(),consumed) )
        print("display info")
        print( displayInfo)
    
    context = {
        'display': displayInfo,
    }
    return render(request, 'consumedPl.html', context)

def showAllLocations(request):
    context = {
        'entity_list': Location.objects.all(),
        'entity_name':'Locations',
    }
    return render(request, 'listLocations.html', context)

def devGround(request):
    context = {
        'entity_list': Animal.objects.all(),
        'entity_name': Animal._meta.fields,
        'attrs':['name'],
    }
    return render(request, 'testGround.html',context)

