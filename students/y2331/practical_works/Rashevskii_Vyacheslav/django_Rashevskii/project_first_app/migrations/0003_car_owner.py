# Generated by Django 3.0.4 on 2020-03-30 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_auto_20200324_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.Owner'),
        ),
    ]