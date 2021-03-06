# Generated by Django 2.2.7 on 2020-04-13 02:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0010_produce_grains_update_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produce',
            name='price',
        ),
        migrations.RemoveField(
            model_name='produce',
            name='sale_quantity',
        ),
        migrations.RemoveField(
            model_name='produce',
            name='unit',
        ),
        migrations.AddField(
            model_name='produce',
            name='fruits_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produce',
            name='fruits_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produce',
            name='fruits_unit',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='produce',
            name='fruits_update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='produce',
            name='grains_unit',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='produce',
            name='oilseeds_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produce',
            name='oilseeds_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produce',
            name='oilseeds_unit',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='produce',
            name='oilseeds_update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='produce',
            name='vegetables_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produce',
            name='vegetables_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produce',
            name='vegetables_unit',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='produce',
            name='vegetables_update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
