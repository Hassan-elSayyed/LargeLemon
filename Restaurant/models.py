from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    def get_item(self):
        return f"{self.title}: {str(self.price)}"
    def __str__(self):
        return f"{self.title}: {str(self.price)}"


class Booking(models.Model):
    tableno = models.IntegerField()
    persons = models.IntegerField()