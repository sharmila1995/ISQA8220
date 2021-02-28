from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Registrant(models.Model):
    Registrant_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.save()

    def updated(self):
        self.save()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=50)
    venue_email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    venue_address = models.CharField(max_length=200)
    venue_city = models.CharField(max_length=50)
    venue_state = models.CharField(max_length=50)
    venue_zipcode = models.CharField(max_length=10)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.save()

    def updated(self):
        self.save()

    def __str__(self):
        return self.venue_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=50)
    event_date = models.DateTimeField()
    event_description = models.CharField(max_length=200)
    event_venue = models.ForeignKey(Venue, on_delete=models.PROTECT, related_name='event')
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.save()

    def updated(self):
        self.save()

    def __str__(self):
        return self.event_name


class Rsvp(models.Model):
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE, related_name='rsvps')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.save()

    def updated(self):
        self.save()

    def save(self, *args, **kwargs):
        self.datetime_created = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        person = self.registrant
        return '{} {}\'s rsvp for {}'.format(person.first_name, person.last_name, self.event.event_name)
