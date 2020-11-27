from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Animal)
admin.site.register(Plant)
admin.site.register(UserAccount)
admin.site.register(Event)
admin.site.register(Sighting)
admin.site.register(UserSightingSaved)
admin.site.register(SightingComment)
admin.site.register(Attends)
admin.site.register(AnimalSighting)
admin.site.register(PlantSighting)
admin.site.register(ConsumeAnimal)
admin.site.register(ConsumePlant)
admin.site.register(Location)
admin.site.register(Flag)
admin.site.register(Lives)