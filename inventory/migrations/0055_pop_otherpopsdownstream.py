# Generated by Django 2.0.7 on 2018-10-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0054_auto_20180919_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='pop',
            name='otherpopsdownstream',
            field=models.ManyToManyField(blank=True, to='inventory.Pop'),
        ),
    ]
