# Generated by Django 2.2.7 on 2020-04-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0007_auto_20200412_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='crop_insurance',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='govt_scheme_enroll',
            field=models.CharField(max_length=64),
        ),
    ]
