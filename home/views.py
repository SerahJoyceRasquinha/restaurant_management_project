from django.shortcuts import render

def index(request):
    context = {
        'restaurant_name' : settings.RESTAURANT_NAME
    }
    return render(request, 'home/index.html')
