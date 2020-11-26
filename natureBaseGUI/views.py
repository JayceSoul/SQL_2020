from django.shortcuts import render
from django.http import HttpResponse

from .models import Animal
# Create your views here.


def index(request):
    html = '<html><body> potato <body></html>'
    return HttpResponse(html)


def pathing(request,input_id):
    return HttpResponse("tester %s " % input_id)


def showAllAnimals(request):
    context = {
        'animal_list': Animal.objects.all()
    }
    return render(request, 'animals.html', context)