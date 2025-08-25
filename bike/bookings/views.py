from django.shortcuts import render

from .models import MyBooking
from django.contrib.auth.decorators import login_required

@login_required
def my_bookings(request):
    bookings = MyBooking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})
