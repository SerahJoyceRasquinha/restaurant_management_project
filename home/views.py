from django.shortcuts import render

def index(request):
    context = {
        'restaurant_name' : settings.RESTAURANT_NAME
        'phone_number' : settings.RESTAURANT_PHONE_NUMBER
    }
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')