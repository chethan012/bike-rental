from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Bike   # import Bike model from mainapp

class MyBooking(models.Model):
    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.bike.name} ({self.payment_status})"
