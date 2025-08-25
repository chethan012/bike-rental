from django.db import models

# Create your models here.
class Bike(models.Model):
  model_name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  rent_per_day = models.PositiveIntegerField()
  availability = models.BooleanField(default=True)
  image = models.ImageField(upload_to='bikes/', null=True, blank=True)
  description = models.TextField(max_length=500, null=True, blank=True)
  
  def __str__(self):
    status = "Available" if self.availability else "Not Available"
    return f"{self.brand} {self.model_name} - ₹{self.rent_per_day}/day ({status})"