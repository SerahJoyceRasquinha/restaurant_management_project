from django.shortcuts import render

def index(request):
    context = {
        'restaurant_name' : settings.RESTAURANT_NAME
    }
    return render(request, 'home/index.html')

def about(request):
    context = {
        'phone_number' : settings.RESTAURANT_PHONE_NUMBER
    }
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def menu(request):
    menu_items = [
       {'name': 'Apple', 'price': 'Rs.30'},
       {'name': 'Orange', 'price': 'Rs.35'}, 
    ]