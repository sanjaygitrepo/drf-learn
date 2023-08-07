from django.db import models

class Department(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length=20)
    dept_code = models.CharField(max_length=5)

class Employee(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete= models.CASCADE)