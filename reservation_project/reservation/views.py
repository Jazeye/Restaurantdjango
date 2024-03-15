from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def reservationtable_view(request):
    return render(request, 'reservationtable.html')

def menu_view(request):
    return render(request, 'menu.html')