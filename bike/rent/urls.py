from django.urls import path 
from . import views
urlpatterns =[
    # path('car/<int:bike_id>/add/', views.addRent, name='addrent'),
    path('add/<int:bike_id>/', views.rentView, name='rentcart'),
    path('update/<int:bike_id>', views.updateBike, name = 'update_bike')
]