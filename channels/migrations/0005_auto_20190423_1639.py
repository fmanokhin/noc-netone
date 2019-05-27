# Generated by Django 2.0.7 on 2019-04-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_remove_device_geoaddress'),
        ('channels', '0004_auto_20190423_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='l2vpn',
            name='pointA',
            field=models.ManyToManyField(blank=True, related_name='l2vpn_pointA', to='inventory.Pop'),
        ),
        migrations.RemoveField(
            model_name='l2vpn',
            name='pointB',
        ),
        migrations.AddField(
            model_name='l2vpn',
            name='pointB',
            field=models.ManyToManyField(blank=True, related_name='l2vpn_pointB', to='inventory.Pop'),
        ),
    ]
