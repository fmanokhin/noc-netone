# Generated by Django 2.0.7 on 2018-09-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0028_network'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='network',
            field=models.CharField(max_length=18),
        ),
    ]
