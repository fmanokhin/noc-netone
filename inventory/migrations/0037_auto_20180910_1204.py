# Generated by Django 2.0.7 on 2018-09-10 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0036_auto_20180907_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='network',
            name='tocore',
        ),
        migrations.RemoveField(
            model_name='network',
            name='tocustomer',
        ),
        migrations.RemoveField(
            model_name='network',
            name='topop',
        ),
    ]