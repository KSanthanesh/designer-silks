# Generated by Django 3.2.9 on 2021-12-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20211220_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line2',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
