# Generated by Django 5.0.7 on 2024-07-14 13:17

import pinger.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(validators=[pinger.models.validate_ip_address])),
            ],
        ),
    ]
