from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Welcome'),
    path('<int:input_id>/', views.pathing, name='test'),
    path('animal/', views.showAllAnimals, name='animals'),
    path('animal/<int:animal_id>/', views.showAnimal, name='animal'),
    path('plant/', views.showAllPlants, name='plants'),
    path('plant/<int:plant_id>/', views.showPlant, name='plant'),
    path('sighting/', views.showAllSightings, name='sightings'),
    path('sighting/<int:sight_id>/', views.showSighting, name='sighting'),    
    path('user/', views.devGround, name='users'),
    path('user/<int:user_id>/', views.showUser, name='user'),
    path('events/',views.showAllEvents,name='events'),
    path('cal/',views.devGround,name='devTest'),
]