# Generated by Django 2.0.7 on 2018-07-30 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='vlans',
            new_name='bandwidth',
        ),
    ]
