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
    try:
        items = MenuItem.objects.all()
    except DatabaseError:
        items = []
        error_message = "Sorry."
        return render(request, 'home/menu.html', {'items': items, 'error': error_message})
    return render(request, 'home/menu.html', {'items': items}) 
    ]