from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('confirm/<int:booking_id>', views.booking_confirm, name = 'confirm_booking'),
    path('success/<int:booking_id>', views.booking_success, name='success_page'),
    path('cancel/<int:booking_id>', views.booking_cancel, name = 'booking_cancel'),
    path('history/', views.booking_history, name='history'),
]