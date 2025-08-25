from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from mainapp.models import Bike   # Bike model is in mainapp
from .models import Booking
from .forms import BookingForm
from django.views.generic import DetailView

from django.urls import reverse


@login_required
def book_bike(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    if not bike.availability:
      # return redirect('bike_not_available')
      return redirect(reverse('bike_na', kwargs={'pk':bike.id}))
      
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.bike = bike
            booking.save()
            return redirect('book_success', booking.id)
    else:
        form = BookingForm()

    return render(request, 'book_bike.html', {'bike': bike, 'form': form})


@login_required
def book_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'book_success.html', {'booking': booking})


class BikeNotAvailable(DetailView):
  template_name = 'bike_not_available.html'
  model = Bike
  context_object_name = 'bike'
  
