from django.shortcuts import render
from django.http import HttpResponse

from .models import Animal, Plant
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
        'plant_info': Plant.objects.get(pk=plant_id),
        'array': attrValuePair,
        'active': attrToDisplay[0],
    }
    return render(request, 'plant.html', context)



def devGround(request):
    context = {
        'entity_list': Animal.objects.all(),
        'entity_name': Animal._meta.fields,
        'attrs':['name'],
    }
    return render(request, 'testGround.html',context)

