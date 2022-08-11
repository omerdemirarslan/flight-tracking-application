from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Flight(models.Model):
    flight_number = models.CharField(max_length=25, db_index=True)
    take_off = models.DateTimeField(null=False)
    landing = models.DateTimeField(null=False)
    destination = models.ForeignKey(to=Airport, related_name='flights_destination', on_delete=models.CASCADE)
    location = models.ForeignKey(to=Airport, related_name='flights_location', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
