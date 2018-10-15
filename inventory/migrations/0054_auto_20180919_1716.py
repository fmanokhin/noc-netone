# Generated by Django 2.0.7 on 2018-09-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0053_auto_20180912_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='core',
            name='bandwidth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='core',
            name='manager',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='core',
            name='vlans',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='core',
            name='contacts',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
