# Generated by Django 2.0.7 on 2018-08-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0026_auto_20180830_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='device',
            name='dnsname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]