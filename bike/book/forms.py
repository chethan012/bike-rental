from django import forms
from datetime import date
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'min':date.today}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'min':date.today}),
        }