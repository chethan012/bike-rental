from django.urls import path
from . import views

urlpatterns = [
    path("my-bookings/", views.my_bookings, name="my_bookings"),
]
