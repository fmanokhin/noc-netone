# Generated by Django 2.0.7 on 2018-09-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0034_auto_20180907_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='status',
            field=models.CharField(choices=[('FREE', 'Свободно'), ('BUSY', 'Занято')], default='FREE', max_length=4),
        ),
    ]
