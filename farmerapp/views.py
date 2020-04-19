from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Grain, Oilseed, Vegetable, Fruit, Farmer, GrainProduce, OilseedProduce, VegetableProduce, FruitProduce

# Create your views here.
@login_required(login_url='login_view')
def index(request):
    
    #check if user is admin (ie anandoghose)
    if not request.user.username == 'anandoghose':
        messages.success(request, 'Sorry, this page is for admins only!')
        
        return HttpResponseRedirect(reverse('login_view'))
    
    #update all records, along with farmer details for:
    grains = GrainProduce.objects.all()
    oilseeds = OilseedProduce.objects.all()
    vegetables = VegetableProduce.objects.all()
    fruits = FruitProduce.objects.all()

    context = {
        'grains': grains,
        'oilseeds': oilseeds,
        'vegetables': vegetables,
        'fruits': fruits,

    }
    return render(request, "farmerapp/index.html", context)

def saleform(request):
    '''form to submit your sale request'''

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

    try:
        int(request.user.username)
    except ValueError:
        return HttpResponseRedirect(reverse('login_view'))
    phone_number = int(request.user.username)
    farmer = Farmer.objects.get(phone_number = phone_number)

    if request.POST['grain_qty'] != "":
        grain = request.POST['grain']
        grain_qty = request.POST['grain_qty']
        grain_unit = request.POST['grain_unit']
        grain_price = request.POST['grain_price']
        grain_comment = request.POST['grain_comment']
        # check if the farmer has entered any qty, if he has then check if he has any existing record:
        try:
            GrainProduce.objects.get(farmer=farmer, grain=grain)
        except GrainProduce.DoesNotExist:
            GrainProduce.objects.create(farmer=farmer, grain=grain, grain_qty=grain_qty, grain_unit=grain_unit, grain_price=grain_price, grain_comment=grain_comment)
            
        produce = GrainProduce.objects.get(farmer=farmer, grain=grain)

        produce.grain_qty = grain_qty
        produce.grain_unit = grain_unit
        produce.grain_price = grain_price
        produce.grain_update_date = timezone.now()
        produce.grain_comment = grain_comment
        produce.save()
        

    if request.POST['oilseed_qty'] != "":
        oilseed = request.POST['oilseed']
        oilseed_qty = request.POST['oilseed_qty']
        oilseed_unit = request.POST['oilseed_unit']
        oilseed_price = request.POST['oilseed_price']
        oilseed_comment = request.POST['oilseed_comment']
        # check if the farmer has entered any qty, if he has then check if he has any existing record:
        try:
            OilseedProduce.objects.get(farmer=farmer, oilseed=oilseed)
        except OilseedProduce.DoesNotExist:
            OilseedProduce.objects.create(farmer=farmer, oilseed=oilseed, oilseed_qty=oilseed_qty, oilseed_unit=oilseed_unit, oilseed_price=oilseed_price, oilseed_comment=oilseed_comment)

        produce = OilseedProduce.objects.get(farmer=farmer, oilseed=oilseed)

        produce.oilseed_qty = oilseed_qty
        produce.oilseed_unit = oilseed_unit
        produce.oilseed_price = oilseed_price
        produce.oilseed_update_date = timezone.now()
        produce.save()   

    if request.POST['vegetable_qty'] != "":
        vegetable = request.POST['vegetable']
        vegetable_qty = request.POST['vegetable_qty']
        vegetable_unit = request.POST['vegetable_unit']
        vegetable_price = request.POST['vegetable_price']
        vegetable_comment = request.POST['vegetable_comment']
        # check if the farmer has entered any qty, if he has then check if he has any existing record:
        try:
            VegetableProduce.objects.get(farmer=farmer, vegetable=vegetable)
        except VegetableProduce.DoesNotExist:
            VegetableProduce.objects.create(farmer=farmer, vegetable=vegetable, vegetable_qty=vegetable_qty, vegetable_unit=vegetable_unit, vegetable_price=vegetable_price, vegetable_comment=vegetable_comment)

        produce = VegetableProduce.objects.get(farmer=farmer, vegetable=vegetable)

        produce.vegetable_qty = vegetable_qty
        produce.vegetable_unit = vegetable_unit
        produce.vegetable_price = vegetable_price
        produce.vegetable_update_date = timezone.now()
        produce.vegetable_comment = vegetable_comment
        produce.save()
    
    if request.POST['fruit_qty'] != "":
        fruit = request.POST['fruit']
        fruit_qty = request.POST['fruit_qty']
        fruit_unit = request.POST['fruit_unit']
        fruit_price = request.POST['fruit_price']
        fruit_comment = request.POST['fruit_comment']
        # check if the farmer has entered any qty, if he has then check if he has any existing record:
        try:
            FruitProduce.objects.get(farmer=farmer, fruit=fruit)
        except FruitProduce.DoesNotExist:
            FruitProduce.objects.create(farmer=farmer, fruit=fruit, fruit_qty=fruit_qty, fruit_unit=fruit_unit, fruit_price=fruit_price, fruit_comment=fruit_comment)

        produce = FruitProduce.objects.get(farmer=farmer, fruit=fruit)

        produce.fruit_qty = fruit_qty
        produce.fruit_unit = fruit_unit
        produce.fruit_price = fruit_price
        produce.fruit_update_date = timezone.now()
        produce.fruit_comment = fruit_comment
        produce.save()

        
    #grain = request.POST["grain"]
    #quantity = int(request.POST['quantity'])
    #unit = request.POST['unit']
    #price = int(request.POST['price'])
    
    messages.success(request, 'Entry Recorded!')
    return HttpResponseRedirect(reverse('saleform'))
    

def register(request):
    
    if request.method == "POST":
        
        #user credentials
        username = request.POST["username"]
        password = username
        email = "test@test.com"

        user = authenticate(request, username=username, password = password)

        if user is not None:
            messages.success(request, 'User already exists. Please use another number.')
            return HttpResponseRedirect(reverse('register'))
        
        else:

            User.objects.create_user(username, email, password)
            user = authenticate(request, username=username, password = password)
            login(request, user)

            #farmer details
            farmer_name = request.POST["name"]
            village = request.POST["village"]
            govt_scheme = request.POST["govtScheme"]
            crop_insurance = request.POST["cropInsurance"]

            Farmer.objects.create(farmer_name=farmer_name, village=village, phone_number=int(username), govt_scheme_enroll=govt_scheme, crop_insurance=crop_insurance)
            messages(request, f"Hello {farmer_name}! | Vaṇakkam! | வணக்கம்")
            return HttpResponseRedirect(reverse('saleform'))
    return render(request, "farmerapp/register.html") 

def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = username
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            phone_number = int(request.user.username)
            farmer = Farmer.objects.get(phone_number = phone_number)
            farmer_name = farmer.farmer_name
            messages.success(request, f"Hello {farmer_name}! | Vaṇakkam! | வணக்கம்!")
            return HttpResponseRedirect(reverse('saleform'))
        else:
            messages.success(request, 'This phone number does not exist in our Database!')
            return HttpResponseRedirect(reverse('login_view'))
    
    return render(request, "farmerapp/login_view.html")
