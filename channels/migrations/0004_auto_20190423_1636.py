# Generated by Django 2.0.7 on 2019-04-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_remove_device_geoaddress'),
        ('channels', '0003_auto_20190423_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='l2vpn',
            name='pointA',
        ),
        migrations.AddField(
            model_name='l2vpn',
            name='pointA',
            field=models.ManyToManyField(blank=True, to='inventory.Pop'),
        ),
    ]
