# Generated by Django 5.1.2 on 2024-10-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_memberinfo_ticket_delete_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
