from django import forms
from .models import Registrant, Event, Venue


class RegistrantForm(forms.ModelForm):
    class Meta:
        model = Registrant
        fields = ('Registrant_id', 'first_name', 'last_name', 'email', 'phone_number',
                  'address', 'city', 'state', 'zipcode')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_id', 'event_name', 'event_date', 'event_description')


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('venue_id', 'venue_name', 'venue_email', 'phone_number',
                  'venue_address', 'venue_city', 'venue_state', 'venue_zipcode')
