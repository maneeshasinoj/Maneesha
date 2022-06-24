from django.db import models
from datetime import datetime,date

# Create your models here.
class employee(models.Model):
    employee_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    email_id=models.EmailField()
    joindate=models.DateField()
    qualification=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)

