from django.db import models
from django.urls import reverse

class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    phone = models.IntegerField()
    joining_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName
    
    def get_absolute_url(self):
        return reverse('all_employees')