from django.urls import path
from . import views


urlpatterns = [
  path('',views.HomeView , name = 'homepage'),  #as_view
  path('about',views.aboutview, name = 'aboutpage'),
  path('contact',views.contactview, name='contactpage'),
  path('bikelist',views.bikelistview, name='bikelist'),
  path('bikes/add/',views.AddBike.as_view(), name='AddBike'),
  path('bikes/update/<int:pk>/',views.UpdateBike.as_view(), name='UpdateBike'),
  path('bikes/Delete/<int:pk>/',views.DeleteBike.as_view(), name='DeleteBike'),
  path('bikes/<int:pk>/',views.BikeDetails.as_view(), name='BikeDetails'),
  
  # path('bookings/', views.mybo, name='BikeList'),
  path('search/', views.searchView, name='search_bikes'),
]