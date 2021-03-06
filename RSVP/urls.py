from django.urls import path, re_path

from . import views

app_name = 'RSVP'
urlpatterns = [path('', views.home, name='home'), re_path(r'^home/$', views.home, name='home'),
               path('registrant_list', views.registrant_list, name='registrant_list'),
               path('registrant/<int:pk>/edit/', views.registrant_edit, name='registrant_edit'),
               path('registrant/<int:pk>/delete/', views.registrant_delete, name='registrant_delete'),
               path('event_list', views.event_list, name='event_list'),
               path('event/<int:event_id>/register', views.event_registration, name='event_registration'),
               path('event/create/', views.event_new, name='event_new'),
               path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
               path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
               path('venue_list', views.venue_list, name='venue_list'),
               path('venue/create/', views.venue_new, name='venue_new'),
               path('venue/<int:pk>/edit/', views.venue_edit, name='venue_edit'),
               path('venue/<int:pk>/delete/', views.venue_delete, name='venue_delete'),
               path('registration/register/', views.register, name='register'),
               ]
