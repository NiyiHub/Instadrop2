from django.db import models
from django.utils import timezone

import random

def parcel_tracking_number():
    return str(random.randint(1000000000, 9999999999))


class AddressDetails(models.Model):

    name                        = models.CharField(max_length=25)
    company                     = models.CharField(max_length=100, null=True, blank=True)
    email                       = models.EmailField()
    address                     = models.CharField(max_length=100)
    city                        = models.CharField(max_length=25)
    states                      = (
                                    ('Abuja', 'Abuja'),
                                    ('Abia', 'Abia'),
                                    ('Akwa Ibom', 'Akwa Ibom'),
                                    ('Anambra', 'Anambra'),
                                    ('Bauchi', 'Bauchi'),
                                    ('Benue', 'Benue'),
                                    ('Borno', 'Borno'),
                                    ('Cross River', 'Cross River'),
                                    ('Delta', 'Delta'),
                                    ('Ebonyi', 'Ebonyi'),
                                    ('Edo', 'Edo'),
                                    ('Ekiti', 'Ekiti'),
                                    ('Enugu', 'Enugu'),
                                    ('Gombe', 'Gombe'),
                                    ('Imo', 'Imo'),
                                    ('Jigawa', 'Jigawa'),
                                    ('Kaduna', 'Kaduna'),
                                    ('Kano', 'Kano'),
                                    ('Katsina', 'Katsina'),
                                    ('Kebbi', 'Kebbi'),
                                    ('Kogi', 'Kogi'),
                                    ('Kwara', 'Kwara'),
                                    ('Lagos', 'Lagos'),
                                    ('Nasarawa', 'Nasarawa'),
                                    ('Niger', 'Niger'),
                                    ('Ogun', 'Ogun'),
                                    ('Ondo', 'Ondo'),
                                    ('Osun', 'Osun'),
                                    ('Oyo', 'Oyo'),
                                    ('Plateau', 'Plateau'),
                                    ('Rivers', 'Rivers'),
                                    ('Sokoto', 'Sokoto'),
                                    ('Taraba', 'Taraba'),
                                    ('Yobe', 'Yobe'),
                                    ('Zamfara', 'Zamfara')
                                    )
    state                       = models.CharField(max_length=25, choices=states)
    mobile                      = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class Parcel(models.Model):

    tracking_number             = models.CharField(max_length=10, unique=True,
                                editable=False, blank=True, default=parcel_tracking_number)
    delivery_date               = models.DateField()
    delivery_address            = models.OneToOneField(AddressDetails, on_delete=models.CASCADE, null=True)
    parcel_content              = models.CharField(max_length=150)
    parcel_weight               = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    sender                      = models.CharField(max_length=25, default="", null=False)
    sender_mobile               = models.CharField(max_length=14, default="", null=False)
    sender_address              = models.CharField(max_length=60, default="", null=False)
    receiver                    = models.CharField(max_length=25, default="", null=False)
    receiver_mobile             = models.CharField(max_length=14, default="", null=False)
    receiver_address            = models.CharField(max_length=60, default="", null=False)
    parcel_typess               = (
                                    ('FILES', 'Files'),
                                    ('PACKAGES', 'Packages')
                                    )
    parcel_type                 = models.CharField(max_length=10, choices=parcel_typess)
    payment_types               = (
                                    ('CASH', 'Cash'),
                                    ('TRANSFER', 'Transfer')
                                    )
    payment_type                = models.CharField(max_length=12, choices=payment_types)
    pickup_date                 = models.DateField(null=True)
    shipment_note               = models.TextField(null=True, blank=True)
    shipping_agents				= (
    								('INSTADROP', 'Instadrop'),
    								('DHL', 'Dhl'),
    								('EMS', 'Ems'),
    								('BUS PARK', 'Bus Park')
    								)
    shipping_agent 				= models.CharField(max_length=9, choices=shipping_agents)

    def __str__(self):
        return self.tracking_number


    def get_absolute_url(self):
        return reverse('parcel-detail', kwargs={'pk': self.pk})


# class History(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 

    


