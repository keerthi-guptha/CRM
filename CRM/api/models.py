from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Enrol(models.Model):
    #creating enrol model for enrollment form
    firstname = models.TextField(max_length = 200,)
    lastname= models.TextField(max_length = 200)
    emailid  = models.EmailField()
    phoneNumber = PhoneNumberField( null = True, blank = False) # Here
    course = models.TextField()

    def __str__(self):
        return self.firstname + " "+ str(self.lastname)+ " "

class Student(models.Model):

    name=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    password= models.CharField(max_length=15)
    email_id=models.EmailField(max_length=30)
    phone_no=models.CharField(max_length=10)
    course=models.CharField(max_length=15)

    def __str__(self):
        return self.name