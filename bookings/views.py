
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Booking
from .forms import BookingForm, ContactMessageForm
from django.contrib import messages
from django.core.mail import send_mail

def home(request):
    properties = Property.objects.filter(available=True)[:4]
    context = {'properties': properties}
    return render(request, 'home.html', context)

def property_list(request):
    properties = Property.objects.filter(available=True)
    context = {'properties': properties}
    return render(request, 'bookings/listings.html', context)

def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    context = {'property': property}
    return render(request, 'bookings/details.html', context)

def booking_view(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if not property.available:
        messages.error(request, 'Sorry, this property is currently unavailable for booking.')
        return redirect('property_detail', property_id=property.id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.property = property
            booking.save()
            subject = 'Your Booking Request - The Grand Address'
            message = f"""
Hello {booking.full_name},

Thank you for choosing The Grand Address!

Your booking request has been received successfully.

BOOKING DETAILS
Property: {booking.property.name}
Location: {booking.property.location}
Booking Date: {booking.booking_date}
Price per Night: ₦{booking.property.price_per_night}
Booking Status: {booking.status}

Our team will contact you regarding your reservation.

Thank you for choosing The Grand Address!
"""
            try:
                send_mail(
                    subject,
                    message,
                    None,
                    [booking.email],
                    fail_silently=False
                )
                return redirect('booking_success', booking_id=booking.id)
            except Exception:
                booking.delete()
                messages.error(request, 'We could not send your confirmation email. Please check your email address and try again.')
                return redirect('booking', property_id=property.id)
    else:
        form = BookingForm()
    context = {'form': form, 'property': property}
    return render(request, 'bookings/booking.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully. Thank you for contacting us!')
            return redirect('contact')
    else:
        form = ContactMessageForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    context = {'booking': booking}
    return render(request, 'bookings/booking_success.html', context)
