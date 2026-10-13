from django.shortcuts import render
from version_1.models import MenuItems
from version_1.models import BusinessHours
from version_1.models import BusinessSettings
# Create your views here.
def home(request):
    menu_items = MenuItems.objects.filter(is_available=True)
    business_hours = BusinessHours.objects.all()
    business_settings = BusinessSettings.objects.first()
    return render(request,"version_1/home.html",{'menu_items':menu_items,'business_hours':business_hours,'business_settings':business_settings})

