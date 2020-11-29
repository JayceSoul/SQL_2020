from django.urls import path

from . import views

urlpatterns = []

urlpatterns = [
    path('', views.index, name='Welcome'),
    path('<int:input_id>/', views.pathing, name='test'),
    path('animal/', views.showAllAnimals, name='animals'),
    path('animal/<int:animal_id>/', views.showAnimal, name='animal'),
    path('plant/', views.showAllPlants, name='plants'),
    path('plant/<int:plant_id>/', views.showPlant, name='plant'),
    path('user/', views.devGround, name='users'),
    path('user/<int:user_id>/', views.showUser, name='user'),
    path('events/',views.showAllEvents,name='events'),
    path('flags/',views.showAllFlags,name='flags'),
    path('consumeAnimal/',views.showConsumeAnimal,name='consumeAnimal'),
    path('consumePlant/',views.showConsumePlant,name='consumePlant'),
    path('locations/',views.showAllLocations,name='locations'),
    path('cal/',views.devGround,name='devTest'),
]