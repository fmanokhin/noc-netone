# Generated by Django 2.0.7 on 2018-07-31 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20180730_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='upstream',
            field=models.ManyToManyField(blank=True, to='inventory.Pop'),
        ),
        migrations.AddField(
            model_name='pop',
            name='downstream',
            field=models.ManyToManyField(blank=True, to='inventory.Customer'),
        ),
    ]
