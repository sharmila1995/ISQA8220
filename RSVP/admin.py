from django.contrib import admin

from .models import Registrant, Event, Venue, Rsvp

class RegistrantList(admin.ModelAdmin):
    list_display = ( 'Registrant_id', 'first_name', 'Last_name', 'phone_number' )
    list_filter = ( 'first_name', 'phone_number')
    search_fields = ('first_name', )
    ordering = ['first_name']

admin.site.register(Registrant)

class VenueList(admin.ModelAdmin):
    list_display = ( 'venue_id', 'Venue_name', 'phone_number' )
    list_filter = ( 'event_name', 'event_date')
    search_fields = ('event_name', )
    ordering = ['event_name']

admin.site.register(Venue)

class EventList(admin.ModelAdmin):
    list_display = ( 'event_id', 'event_name', 'event_date', 'event_description' )
    list_filter = ( 'event_name', 'event_date')
    search_fields = ('event_name', )
    ordering = ['event_name']

admin.site.register(Event)

class RsvpList(admin.ModelAdmin):
    list_display = ['__str__', 'created_date']
    list_filter = ()
    search_fields = []
    ordering = ['datetime_created']

admin.site.register(Rsvp)