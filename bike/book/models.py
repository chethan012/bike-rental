from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Bike

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def total_days(self):
        return (self.end_date - self.start_date).days + 1

    def total_price(self):
        return self.total_days() * self.bike.price

    def __str__(self):
        return f"{self.user.username} booked {self.bike.name}"

