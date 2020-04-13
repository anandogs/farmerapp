from django.contrib import admin

# Register your models here.
from .models import Produce, Farmer, Grain, Oilseed, Vegetable, Fruit

admin.site.register(Produce)
admin.site.register(Farmer)
admin.site.register(Grain)
admin.site.register(Oilseed)
admin.site.register(Vegetable)
admin.site.register(Fruit)
