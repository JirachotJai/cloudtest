# Generated by Django 5.1.2 on 2024-10-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_location_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberinfo',
            name='ticket',
            field=models.ManyToManyField(to='tickets.ticket'),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
