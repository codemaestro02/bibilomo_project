# Generated by Django 5.1.4 on 2024-12-19 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_contactmessage_flightpackage_date_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightpackage',
            name='placeholder_image',
            field=models.ImageField(upload_to='flight_images'),
        ),
    ]
