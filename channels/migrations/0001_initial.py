# Generated by Django 2.0.7 on 2019-04-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='L2VPN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelid', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=100)),
                ('pointA', models.CharField(blank=True, max_length=1000)),
                ('pointB', models.CharField(blank=True, max_length=1000)),
                ('comments', models.TextField(blank=True, max_length=1000)),
                ('on_date', models.DateField(blank=True, null=True)),
                ('off_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]