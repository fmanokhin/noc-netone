# Generated by Django 2.0.7 on 2018-07-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_core_downstream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core',
            name='downstream',
            field=models.ManyToManyField(blank=True, null=True, to='inventory.Pop'),
        ),
    ]