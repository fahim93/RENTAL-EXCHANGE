# Generated by Django 3.1.2 on 2020-10-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_exchange', '0008_auto_20201010_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='features',
            field=models.ManyToManyField(blank=True, to='rental_exchange.Feature'),
        ),
    ]
