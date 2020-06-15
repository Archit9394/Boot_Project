from django.db import models

# Create your models here.
class info(models.Model):
    name=models.CharField(max_length=50)
    id=models.AutoField(primary_key=True)
    contact=models.CharField(max_length=10)
    address=models.CharField(max_length=250)