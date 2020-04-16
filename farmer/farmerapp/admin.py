from django.contrib import admin

# Register your models here.
from .models import Farmer, Grain, Oilseed, Vegetable, Fruit, GrainProduce, OilseedProduce, VegetableProduce, FruitProduce

admin.site.register(GrainProduce)
admin.site.register(OilseedProduce)
admin.site.register(VegetableProduce)
admin.site.register(FruitProduce)
admin.site.register(Farmer)
admin.site.register(Grain)
admin.site.register(Oilseed)
admin.site.register(Vegetable)
admin.site.register(Fruit)
