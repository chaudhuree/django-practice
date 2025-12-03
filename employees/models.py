from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    email = models.EmailField(max_length=100,unique=True)
    designation = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15,blank=True)  # phone number is optional
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
     