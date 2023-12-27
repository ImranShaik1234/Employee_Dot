from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=100)
    emp_ID = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.CharField(max_length=100)
