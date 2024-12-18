from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    Gender = models.CharField(max_length=30)
    YOP = models.IntegerField()
    Age = models.IntegerField()
    Skills = models.CharField(max_length=1000)
    DOB = models.DateField()
    Address = models.CharField(max_length=100)
    Mock_Rating = models.CharField(max_length=10, default='0')
    Company = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
