# Generated by Django 2.0.7 on 2018-07-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20180724_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pop',
            name='upstream',
            field=models.ManyToManyField(blank=True, null=True, to='inventory.Core'),
        ),
    ]
