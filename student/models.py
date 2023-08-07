from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True)
    mobile_number = models.CharField(max_length=20,unique=True)
    rollno = models.IntegerField(unique=True)
    admission_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name+" "+self.last_name
