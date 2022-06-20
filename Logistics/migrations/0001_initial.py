# Generated by Django 4.0.5 on 2022-06-20 01:16

import Logistics.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(blank=True, default=Logistics.models.parcel_tracking_number, editable=False, max_length=10, unique=True)),
                ('delivery_date', models.DateField()),
                ('parcel_content', models.CharField(max_length=150)),
                ('parcel_weight', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('sender', models.CharField(default='', max_length=25)),
                ('sender_mobile', models.CharField(default='', max_length=14)),
                ('sender_address', models.CharField(default='', max_length=60)),
                ('receiver', models.CharField(default='', max_length=25)),
                ('receiver_mobile', models.CharField(default='', max_length=14)),
                ('receiver_address', models.CharField(default='', max_length=60)),
                ('parcel_type', models.CharField(choices=[('FILES', 'Files'), ('PACKAGES', 'Packages')], max_length=10)),
                ('payment_type', models.CharField(choices=[('CASH', 'Cash'), ('TRANSFER', 'Transfer')], max_length=12)),
                ('pickup_date', models.DateField(null=True)),
                ('shipment_note', models.TextField(blank=True, null=True)),
                ('shipping_agent', models.CharField(choices=[('INSTADROP', 'Instadrop'), ('DHL', 'Dhl'), ('EMS', 'Ems'), ('BUS PARK', 'Bus Park')], max_length=9)),
                ('delivery_address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Logistics.addressdetails')),
            ],
        ),
    ]
