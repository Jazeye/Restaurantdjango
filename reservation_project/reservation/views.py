from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from . import forms,models


def index(request):
    products = Reservation.objects.all()
    return render(request, 'index.html', {'products': products})
def reservationtable_view(request):
    return render(request, 'reservationtable.html')

def menu_view(request):
    return render(request, 'menu.html')

#form reservation
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_table')  # Redirect to the same page after submission
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = ReservationForm()
    
    reservations = Reservation.objects.all()  # Fetch all reservations from the database
    return render(request, 'reservationtable.html', {'form': form, 'reservations': reservations})