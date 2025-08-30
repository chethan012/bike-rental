from django.db import models
from mainapp.models import Bike
from django.contrib.auth.models import User

class RentItem(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        if self.start_date and self.end_date:
            days = (self.end_date - self.start_date).days
            if days <= 0:
                return self.bike.rent_per_day # one-day minimum
            return days * self.bike.rent_per_day
        return 0

    def __str__(self):
        return f"{self.user.username} rented {self.bike.model_name if self.bike else 'Bike'}"
