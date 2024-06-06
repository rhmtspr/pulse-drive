from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    STATUS = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('under maintenance', 'Under maintenance')
    ]

    TRANSMISSION = [
        ("manual", "Manual"),
        ("automatic", "Automatic")
    ]

    brand = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    year = models.IntegerField()
    capacity = models.IntegerField()
    price = models.IntegerField(null=True)
    max_power = models.IntegerField(blank=True, null=True)
    top_speed = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION)
    status = models.CharField(max_length=50, choices=STATUS, default="Available")
    image = models.ImageField(upload_to="cars", blank=True, null=True)

    def __str__(self):
        return self.car_type
    

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_price = models.IntegerField(blank=True, null=True)
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField()