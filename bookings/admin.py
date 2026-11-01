from django.contrib import admin
from .models import Property, Booking, SavedProperty, ContactMessage

#Register your models here
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_night', 'available')
    list_editable = ('available',)
    list_filter = ('available', 'location')
    search_fields = ('name', 'location')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'property', 'booking_date', 'status', 'date_created')
    list_filter = ('status', 'booking_date', 'date_created')
    search_fields = ('full_name', 'email', 'phone_number', 'property__name')
    list_editable = ('status',)
    
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'subject', 'date_created')
    list_filter = ('subject', 'date_created')
    search_fields = ('first_name', 'last_name', 'email', 'subject')

admin.site.register(Property, PropertyAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(SavedProperty)
admin.site.register(ContactMessage, ContactMessageAdmin)