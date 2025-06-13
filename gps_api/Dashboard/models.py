from django.db import models
from django.contrib.auth.models import User


class user_Details(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='details')
    is_company_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=100,null=True,blank=True)
    gov_No = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    contact_No = models.CharField(max_length=10,null=True,blank=True)
    role = models.CharField(max_length=10, null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_Picture = models.ImageField(upload_to='profile-picture/',default="null")


class images(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='profile_picture')
    profile_Picture = models.ImageField(upload_to='profile-picture/',default="null")




class company_Details(models.Model):
    admin = models.ForeignKey(User, on_delete= models.CASCADE, related_name='company_Admin')
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=15, blank=True, null=True)
    company_emial = models.EmailField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    parameter = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    descreption = models.TextField(blank=True, null=True)