# Generated by Django 5.1.2 on 2024-10-13 12:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_alter_event_event_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OTHER', 'Other')], default='OTHER', max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=10)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets_memberinfo_member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
