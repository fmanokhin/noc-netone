# Generated by Django 2.0.7 on 2018-09-10 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0047_auto_20180910_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='core',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Core'),
        ),
        migrations.AddField(
            model_name='network',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Customer'),
        ),
        migrations.AddField(
            model_name='network',
            name='pop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Pop'),
        ),
    ]
