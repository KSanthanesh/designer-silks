# Generated by Django 3.2.9 on 2021-12-21 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_house_number', models.CharField(blank=True, max_length=10, null=True)),
                ('default_address_line1', models.CharField(blank=True, max_length=50, null=True)),
                ('default_address_line2', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('default_county_or_city', models.CharField(blank=True, max_length=30, null=True)),
                ('default_postcode', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]