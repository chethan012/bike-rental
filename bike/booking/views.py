from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from mainapp.models import Bike
from datetime import datetime
from rent.models import RentItem
# Create your views here.
@login_required
def create_booking(request):
    rent_item = RentItem.objects.get(user = request.user)

    start_date = rent_item.start_date
    end_date = rent_item.end_date
    total_cost = rent_item.total_price
    print(total_cost)
    bike = rent_item.bike 
    

    booking = Booking.objects.create(
        user=request.user,
        bike=bike,
        start_date=start_date,
        end_date=end_date,
        total_cost=total_cost
    )
    print("Booking done. Redirecting to confirm booking...")
    # Instead of direct redirect, show success page with "Pay Now" link
    return redirect('booking:confirm_booking', booking_id=booking.id)

def booking_confirm(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    template = 'booking_confirm.html'
    context  = {
       'booking' : booking, 
       'user'    : booking.user,
       'bike'     : booking.bike,
    }
    return render(request, template, context)

def booking_success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'rent_confirm.html', {'booking': booking})

def booking_cancel(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.status = 'cancelled'
    booking.save()
    return redirect('booking:history')


@login_required
def booking_history(request):
    histories = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'bookings': histories})

