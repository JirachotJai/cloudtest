# Generated by Django 5.1.2 on 2024-10-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_memberinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/location/'),
        ),
    ]