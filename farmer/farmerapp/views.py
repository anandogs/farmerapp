from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Produce, Grain, Oilseed, Vegetable, Fruit, Farmer

# Create your views here.
def index(request):
    
    context = {
        "produce": Produce.objects.all()
    }
    return render(request, "farmerapp/index.html", context)

def saleform(request):

    if request.user.is_authenticated:

        context = {
            'grains': Grain.objects.all(),
            'oilseeds': Oilseed.objects.all(),
            'vegetables': Vegetable.objects.all(),
            'fruits': Fruit.objects.all()
        }

        return render(request, "farmerapp/saleform.html", context)
    
    return render(request, "farmerapp/login_view.html")
    

def salereq(request):

    phone_number = int(request.user.username)
    farmer = Farmer.objects.get(phone_number = phone_number)

    if request.POST['grain_qty'] != "":
        grain = request.POST['grain']
        grain_qty = request.POST['grain_qty']
        grain_unit = request.POST['grain_unit']
        grain_price = request.POST['grain_price']
        # check if the farmer has entered any qty, if he has then check if he has any existing record:
        try:
            Produce.objects.get(farmer=farmer)
        except Produce.DoesNotExist:
            Produce.objects.create(farmer=farmer, grain=grain, grain_qty=grain_qty, grain_unit=grain_unit, grain_price=grain_price)
            return HttpResponse('produce created')
        # if the product exists, then update the produce record

        produce = Produce.objects.get(farmer=farmer)

        if produce.grain == "":

            produce.grain_qty = grain_qty
            produce.grain_unit = grain_unit
            produce.grain_price = grain_price
            produce.grain_update_date = timezone.now()
            produce.save()
        
        else:

            Produce.objects.create(farmer=farmer, grain=grain, grain_qty=grain_qty, grain_unit=grain_unit, grain_price=grain_price)
            
    #grain = request.POST["grain"]
    #quantity = int(request.POST['quantity'])
    #unit = request.POST['unit']
    #price = int(request.POST['price'])

    return HttpResponse(farmer.village)
#    

    

def register(request):
    
    if request.method == "POST":
        
        #user credentials
        username = request.POST["username"]
        password = username
        email = "test@test.com"

        User.objects.create_user(username, email, password)

        user = authenticate(request, username=username, password = password)
        login(request, user)

        #farmer details
        farmer_name = request.POST["name"]
        village = request.POST["village"]
        govt_scheme = request.POST["govtScheme"]
        crop_insurance = request.POST["cropInsurance"]

        Farmer.objects.create(farmer_name=farmer_name, village=village, phone_number=int(username), govt_scheme_enroll=govt_scheme, crop_insurance=crop_insurance)

        return HttpResponseRedirect(reverse('saleform'))
    return render(request, "farmerapp/register.html") 

def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = username
        user = authenticate(request, username = username, password = password)
        login(request,user)

        return HttpResponseRedirect(reverse('saleform'))
    
    return render(request, "farmerapp/login_view.html")
