# Generated by Django 2.0.7 on 2018-08-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_auto_20180829_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pop',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]