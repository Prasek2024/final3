

from django.db import models

class Device(models.Model):
    type = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    OAM_address = models.CharField(max_length=200)
    date_added = models.DateField()


    def __str__(self):
        return self.title




# Create your models here.
