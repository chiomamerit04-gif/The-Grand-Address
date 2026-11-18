
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.dateparse import parse_date
from django.db import transaction
from django.conf import settings

from .models import Property, Booking
from .forms import BookingForm, ContactMessageForm

import requests


def home(request):
    properties = Property.objects.filter(available=True)[:4]
    context = {'properties': properties}
    return render(request, 'home.html', context)


def property_list(request):
    properties = Property.objects.filter(available=True)

    location = request.GET.get('location', '').strip()
    checkin = request.GET.get('checkin', '')
    checkout = request.GET.get('checkout', '')
    guests = request.GET.get('guests', '2')

    date_error = ''

    # Filter by destination
    if location:
        properties = properties.filter(location__icontains=location)

    # Filter by guest capacity
    try:
        guest_count = int(guests)

        if guest_count > 0:
            properties = properties.filter(guests__gte=guest_count)

    except (ValueError, TypeError):
        guests = '2'

    # Check booking date availability
    if checkin or checkout:
        checkin_date = parse_date(checkin)
        checkout_date = parse_date(checkout)

        if not checkin_date or not checkout_date:
            date_error = 'Please select both check-in and check-out dates.'

        elif checkout_date <= checkin_date:
            date_error = 'Check-out must be after check-in.'

        else:
            booked_properties = Booking.objects.filter(
                status__in=['Pending', 'Confirmed'],
                check_in__lt=checkout_date,
                check_out__gt=checkin_date
            ).values_list('property_id', flat=True)

            # Temporary debugging information
            print("BOOKED PROPERTY IDS:", list(booked_properties))
            print("SEARCH DATES:", checkin_date, checkout_date)

            properties = properties.exclude(
                id__in=booked_properties
            )

    context = {
        'properties': properties,
        'location': location,
        'checkin': checkin,
        'checkout': checkout,
        'guests': guests,
        'date_error': date_error,
    }

    return render(request, 'bookings/listings.html', context)


def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    context = {'property': property}
    return render(request, 'bookings/details.html', context)


def booking_view(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if not property.available:
        messages.error(
            request,
            'Sorry, this property is currently unavailable for booking.'
        )
        return redirect('property_detail', property_id=property.id)

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.property = property

            with transaction.atomic():
                locked_property = Property.objects.select_for_update().get(
                    id=property.id
                )

                if not locked_property.available:
                    messages.error(
                        request,
                        'Sorry, this property is currently unavailable.'
                    )
                    return redirect(
                        'property_detail',
                        property_id=property.id
                    )

                overlapping_bookings = Booking.objects.filter(
                    property=locked_property,
                    status__in=['Pending', 'Confirmed'],
                    check_in__lt=booking.check_out,
                    check_out__gt=booking.check_in
                )

                if overlapping_bookings.exists():
                    form.add_error(
                        None,
                        'Sorry, this property is already booked for some or all of your selected dates. Please choose different dates.'
                    )

                    return render(request, 'bookings/booking.html', {
                        'form': form,
                        'property': property
                    })

                booking.property = locked_property
                booking.save()

            # Calculate booking price
            nights = (booking.check_out - booking.check_in).days
            total_price = booking.property.price_per_night * nights

            subject = 'Your Booking Request - The Grand Address'

            email_message = f"""
Hello {booking.full_name},

Thank you for choosing The Grand Address!

Your booking request has been received successfully.

BOOKING DETAILS

Property: {booking.property.name}
Location: {booking.property.location}
Check-in: {booking.check_in}
Check-out: {booking.check_out}
Number of Nights: {nights}
Price per Night: ₦{booking.property.price_per_night:,.2f}
Total Price: ₦{total_price:,.2f}
Booking Status: {booking.status}

Our team will contact you regarding your reservation.

Thank you for choosing The Grand Address!
"""

            # Send booking confirmation using Resend API
            try:
                response = requests.post(
                    'https://api.resend.com/emails',
                    headers={
                        'Authorization': f'Bearer {settings.RESEND_API_KEY}',
                        'Content-Type': 'application/json',
                    },
                    json={
                        'from': settings.DEFAULT_FROM_EMAIL,
                        'to': [booking.email],
                        'subject': subject,
                        'text': email_message,
                    },
                    timeout=10,
                )

                response.raise_for_status()

            except requests.exceptions.RequestException as e:
                print("BOOKING EMAIL ERROR:", e)

                if 'response' in locals() and response is not None:
                    print("RESEND RESPONSE:", response.text)

                messages.warning(
                    request,
                    'Your booking was saved, but we could not send your confirmation email.'
                )

            return redirect(
                'booking_success',
                booking_id=booking.id
            )

    else:
        form = BookingForm()

    context = {
        'form': form,
        'property': property
    }

    return render(request, 'bookings/booking.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your message has been sent successfully. Thank you for contacting us!'
            )

            return redirect('contact')

    else:
        form = ContactMessageForm()

    context = {'form': form}
    return render(request, 'contact.html', context)


def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    context = {
        'booking': booking
    }

    return render(
        request,
        'bookings/booking_success.html',
        context
    )
