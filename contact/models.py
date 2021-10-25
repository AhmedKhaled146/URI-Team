from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import EmailField

# Create your models here.
available = [
    ('Any Time', 'Any Time'),
    ('12 am - 6 am', '12 am - 6 am'),
    ('6 am - 12 pm', '6 am - 12 pm'),
    ('12 pm - 6 pm', '12 pm - 6 pm'),
    ('6 pm - 12 am', '6 pm - 12 am'),
]


class ContactInfo(models.Model):
    city_country = models.CharField(max_length=50)
    street = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    available_Time = models.CharField(max_length=15, choices=available)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email
