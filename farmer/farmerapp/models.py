'''Models to make the farmer app work'''
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Grain(models.Model):
    '''Used to populate drop down values for farmer to select from in sale form'''
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Oilseed(models.Model):
    '''Used to populate drop down values for farmer to select from in sale form'''
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Vegetable(models.Model):
    '''Used to populate drop down values for farmer to select from in sale form'''
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Fruit(models.Model):
    '''Used to populate drop down values for farmer to select from in sale form'''
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Farmer(models.Model):
    '''Farmer registration table'''
    farmer_name = models.CharField(max_length=64)
    village = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    govt_scheme_enroll = models.CharField(max_length=64)
    crop_insurance = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.farmer_name}: {self.phone_number}"

class Produce(models.Model):
    '''Produce / Sale table'''
    farmer = models.ForeignKey(Farmer, on_delete="DO_NOTHING")
    grain = models.CharField(max_length=64, default="")
    grain_qty = models.IntegerField(default=0)
    grain_unit = models.CharField(max_length=5, default="")
    grain_price = models.IntegerField(default=0)
    grain_update_date = models.DateTimeField(default=now)
    oilseed = models.CharField(max_length=64, default="")
    oilseed_qty = models.IntegerField(default=0)
    oilseed_unit = models.CharField(max_length=5, default="")
    oilseed_price = models.IntegerField(default=0)
    oilseed_update_date = models.DateTimeField(default=now)
    vegetable = models.CharField(max_length=64, default="")
    vegetable_qty = models.IntegerField(default=0)
    vegetable_unit = models.CharField(max_length=5, default="")
    vegetable_price = models.IntegerField(default=0)
    vegetable_update_date = models.DateTimeField(default=now)
    fruit = models.CharField(max_length=64, default="")
    fruit_qty = models.IntegerField(default=0)
    fruit_unit = models.CharField(max_length=5, default="")
    fruit_price = models.IntegerField(default=0)
    fruit_update_date = models.DateTimeField(default=now)
    comment = models.TextField(default="")

    class Meta:
        verbose_name_plural = "Produce"

    def __str__(self):
        return f"{self.grain}{self.oilseed}{self.vegetable}{self.fruit}"
