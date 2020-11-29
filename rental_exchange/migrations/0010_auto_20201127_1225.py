# Generated by Django 3.1.2 on 2020-11-27 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental_exchange', '0009_carregistrationrequest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'BLOGS'},
        ),
        migrations.AlterField(
            model_name='car',
            name='price_variable',
            field=models.CharField(choices=[('Month', 'Month')], default='Month', max_length=20),
        ),
        migrations.AlterModelTable(
            name='carregistrationrequest',
            table='car_registration_requests',
        ),
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('rent_for', models.CharField(choices=[('3', '3 Months'), ('4', '4 Months'), ('5', '5 Months'), ('6', '6 Months'), ('7', '7 Months'), ('8', '8 Months'), ('9', '9 Months'), ('10', '10 Months'), ('11', '11 Months'), ('12', '12 Months')], max_length=50)),
                ('is_seen', models.BooleanField(default=False)),
                ('request_status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=50)),
                ('rent_status', models.CharField(blank=True, choices=[('On Going', 'On Going'), ('Closed', 'Closed')], max_length=50, null=True)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_exchange.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CAR BOOKING',
                'db_table': 'car_booking',
                'ordering': ('created_at',),
            },
        ),
    ]