from django import forms
from datetime import date
from .models import Booking, ContactMessage

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone_number', 'booking_date', 'special_requests']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+234 800 000 0000'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Any additional requests?'}),
        }

    def clean_booking_date(self):
        booking_date = self.cleaned_data['booking_date']
        if booking_date < date.today():
            raise forms.ValidationError("Please select today or a future date.")
        return booking_date
    
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Your last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+234 800 000 0000'}),
            'subject': forms.Select(),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us how we can help...'}),
        }