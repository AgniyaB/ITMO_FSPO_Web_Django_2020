# Generated by Django 3.0.6 on 2020-06-07 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20200607_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew_member',
            name='id_flight',
        ),
        migrations.RemoveField(
            model_name='flight_information',
            name='id_helicopter',
        ),
    ]
