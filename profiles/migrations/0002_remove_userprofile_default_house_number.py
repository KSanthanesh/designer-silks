# Generated by Django 3.2.9 on 2022-01-17 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_house_number',
        ),
    ]
