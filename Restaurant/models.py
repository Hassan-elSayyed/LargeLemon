from django.db import models
from datetime import date


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    def get_item(self):
        return f"{self.title}: {str(self.price)}"
    def __str__(self):
        return f"{self.title}: {str(self.price)}"


class Booking(models.Model):
    # first_name = models.CharField(max_length=200, default=None)
    # last_name = models.CharField(max_length=200, default=None)
    name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    tableno = models.IntegerField(null=True, blank=True)
    persons = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
