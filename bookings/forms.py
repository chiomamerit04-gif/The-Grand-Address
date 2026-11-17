from django import forms
from datetime import date
from .models import Booking, ContactMessage


class BookingForm(forms.ModelForm):
    check_in = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    check_out = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    class Meta:
        model = Booking
        fields = [
            'full_name',
            'email',
            'phone_number',
            'check_in',
            'check_out',
            'special_requests'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+234 800 000 0000'
            }),
            'special_requests': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Any additional requests?'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        today = date.today().isoformat()

        self.fields['check_in'].widget.attrs['min'] = today
        self.fields['check_out'].widget.attrs['min'] = today
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_in < date.today():
            self.add_error('check_in', 'Please select today or a future date.')

        if check_in and check_out and check_out <= check_in:
            self.add_error('check_out', 'Check-out must be after check-in.')

        return cleaned_data

    def save(self, commit=True):
        booking = super().save(commit=False)
        booking.booking_date = booking.check_in

        if commit:
            booking.save()
            self.save_m2m()

        return booking    
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