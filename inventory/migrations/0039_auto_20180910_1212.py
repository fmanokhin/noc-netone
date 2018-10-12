# Generated by Django 2.0.7 on 2018-09-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0038_auto_20180910_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='tocore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Core'),
        ),
        migrations.AddField(
            model_name='network',
            name='tocustomer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Customer'),
        ),
        migrations.AddField(
            model_name='network',
            name='topop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Pop'),
        ),
    ]