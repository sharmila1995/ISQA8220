# Generated by Django 2.0.5 on 2021-01-31 01:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP', '0003_auto_20210121_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('event_date', models.DateTimeField()),
                ('event_description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvp', to='RSVP.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='events',
            name='event_venue',
        ),
        migrations.RenameField(
            model_name='registrant',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='registrant',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='email',
            new_name='venue_email',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='Venue_id',
            new_name='venue_id',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='Venue_name',
            new_name='venue_name',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='registrant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvp', to='RSVP.Registrant'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event', to='RSVP.Venue'),
        ),
    ]
