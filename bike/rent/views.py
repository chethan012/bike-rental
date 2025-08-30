from django.shortcuts import render, redirect, get_object_or_404
from .models import RentItem
from mainapp.models import Bike
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def rentView(request, bike_id):
    # Get or create a rent item for this user
    item, created = RentItem.objects.get_or_create(user=request.user)
    this_bike = get_object_or_404(Bike, id=bike_id)

    # If user already has a bike, check if it’s different
    if item.bike:
        if item.bike != this_bike:
            return redirect('update_bike', bike_id=bike_id)
    else:
        item.bike = this_bike

    error_message = None

    if request.method == 'POST':
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            today = timezone.now().date()

            if start_date < today:
                error_message = "Start date cannot be in the past."
            elif end_date < start_date:
                error_message = "End date cannot be before start date."
            else:
                item.start_date = start_date
                item.end_date = end_date
                item.save()
                return redirect('booking:create_booking')

        except ValueError:
            error_message = "Invalid date format."

    item.save()
    
    # ✅ Calculate total price (you must define total_price property in RentItem model)
    total_price = item.total_price if hasattr(item, "total_price") else 0  

    template = 'rent_confirm.html'
    context = {
        'item': item,
        'total': total_price,
        'error_message': error_message,
        'price_per_day': item.bike.rent_per_day,
        'bike_name': item.bike.model_name,       
        'today': timezone.now().date().isoformat(),  
    }
    return render(request, template, context)


@login_required
def updateBike(request, bike_id):
    template = 'update_bike.html'
    rentItem = RentItem.objects.get(user=request.user)
    new_bike = get_object_or_404(Bike, id=bike_id)

    context = {
        'curr_bike': rentItem.bike,
        'new_bike': new_bike,
    }

    if request.method == 'POST':
        rentItem.bike = new_bike
        rentItem.save()
        return redirect('rent_bike', bike_id=bike_id)

    return render(request, template, context)
