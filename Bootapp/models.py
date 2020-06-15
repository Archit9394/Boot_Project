from django.db import models

# Create your models here.
class info(models.Model):
    name=models.CharField(max_length=50)
    id=models.AutoField(primary_key=True)
    contact=models.CharField(max_length=10)
    address=models.CharField(max_length=250) 

class city(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=16)

class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    city_id = models.ForeignKey(city, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    confirmation_code = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    time_joined = models.DateTimeField()
    
class restaurants(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    city_id = models.ForeignKey(city,on_delete=models.CASCADE)