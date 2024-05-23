# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# class CustomUser(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('customer', 'Customer'),
#         ('shop_owner', 'Recycle Shop Owner'),
#         ('admin', 'Admin'),
#     )
#     user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='customer')

# Create your models here.
class Login(models.Model):
    name = models.EmailField()
    pswrd = models.CharField(max_length=16)

class Signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    confirm_password = models.CharField(max_length=16)

class QNA(models.Model):
    questions = models.CharField(max_length=1000)
    answers = models.CharField(max_length=10000)
    
class Index_gmails(models.Model):
    emails = models.EmailField()

class Owner(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    # about = models.CharField(max_length=200, null=True)
    organisation_id = models.IntegerField(primary_key=True, max_length=100, default=None)
    organisation_name = models.CharField(max_length=200)
    phone = models.IntegerField()

    street = models.CharField(max_length=400, null=True, default="")
    city = models.CharField(max_length=400, null=True, default="")
    state = models.CharField(max_length=400, null=True, default="")
    zipcode = models.CharField(max_length=400, null=True, default="")
    latitude = models.FloatField()
    longitude = models.FloatField()

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.CharField(max_length=3000)

class RecycleForm(models.Model):
    organisation_id = models.CharField(max_length=100, default=1)
    organisation_name = models.CharField(max_length=100, default='Empty')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    price= models.IntegerField()
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recycle_images/', null=True)
    phone = models.IntegerField()
    facility = models.CharField(max_length=20)
