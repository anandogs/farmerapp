# Generated by Django 2.2.7 on 2020-04-13 01:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0009_auto_20200413_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce',
            name='grains_update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
