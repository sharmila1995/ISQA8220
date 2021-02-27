from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


now = timezone.now()


def home(request):
    return render(request, 'RSVP/home.html',
                  {'RSVP': home})


@login_required
def registrant_list(request):
    registrant = Registrant.objects.filter(created_date__lte=timezone.now())
    return render(request, 'RSVP/registrant_list.html',
                  {'registrants': registrant})


@login_required
def registrant_edit(request, pk):
    registrant = get_object_or_404(Registrant, pk=pk)
    if request.method == "POST":
        # update
        form = RegistrantForm(request.POST, instance=registrant)
        if form.is_valid():
            registrant = form.save(commit=False)
            registrant.updated_date = timezone.now()
            registrant.save()
            registrant = Registrant.objects.filter(created_date__lte=timezone.now())
        return render(request, 'RSVP/registrant_list.html',
                      {'registrants': registrant})
    else:
        # edit
        form = RegistrantForm(instance=registrant)
        return render(request, 'RSVP/registrant_edit.html', {'form': form})


@login_required
def registrant_delete(request, pk):
    registrant = get_object_or_404(Registrant, pk=pk)
    registrant.delete()
    return redirect('RSVP:registrant_list')


@login_required
def event_list(request):
    event = Event.objects.filter(created_date__lte=timezone.now())
    return render(request, 'RSVP/event_list.html',
                  {'events': event})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        # update
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.updated_date = timezone.now()
            event.save()
            event = Event.objects.filter(created_date__lte=timezone.now())
        return render(request, 'RSVP/event_list.html',
                      {'events': event})
    else:
        # edit
        form = EventForm(instance=event)
        return render(request, 'RSVP/event_edit.html', {'form': form})


@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('RSVP:event_list')


@login_required
def venue_list(request):
    venue = Venue.objects.filter(created_date__lte=timezone.now())
    return render(request, 'RSVP/venue_list.html',
                  {'venues': venue})


@login_required
def venue_edit(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    if request.method == "POST":
        # update
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.updated_date = timezone.now()
            venue.save()
            venue = Venue.objects.filter(created_date__lte=timezone.now())
        return render(request, 'RSVP/venue_list.html',
                      {'venues': venue})
    else:
        # edit
        form = VenueForm(instance=venue)
        return render(request, 'RSVP/venue_edit.html', {'form': form})


@login_required
def venue_delete(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    venue.delete()
    return redirect('RSVP:venue_list')
