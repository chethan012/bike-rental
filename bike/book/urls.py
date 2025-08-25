from django.urls import path
from . import views

urlpatterns = [
    path('<int:bike_id>/', views.book_bike, name='book_bike'),
    path('success/<int:booking_id>/', views.book_success, name='book_success'),
    path('bike_na/<int:pk>/', views.BikeNotAvailable.as_view(), name='bike_na')
]
