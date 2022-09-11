import profile
from pyexpat import model
from django.db import models
import datetime

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    access_token = models.CharField(max_length=1000)
    public_id = models.CharField(max_length=1000)
    profession = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    profile_photo = models.FileField()
    profile_photo_path = models.CharField(max_length=500)
    status = models.IntegerField()
    created_at = models.DateTimeField(datetime.datetime.now(), null=True)
    updated_at = models.DateTimeField(datetime.datetime.now(), null=True)






class Journey(models.Model):
    travelling_from = models.CharField(max_length=200)
    travelling_to = models.CharField(max_length=200)
    travelling_date = models.DateField()
    user = models.ForeignKey(Person , on_delete=models.CASCADE)
    status = models.IntegerField()
    created_at = models.DateTimeField(datetime.datetime.now() , null=True)
    updated_at = models.DateTimeField(datetime.datetime.now(), null=True)





class Topics(models.Model):
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=1000)
    photo_file = models.FileField()
    photo_file_path = models.CharField(max_length=1000)
    attach_file = models.FileField()
    attach_file_path = models.CharField(max_length=1000)
    status = models.IntegerField()
    category = models.CharField(max_length=200)
    topic_type = models.CharField(max_length=200)
    user = models.ForeignKey(Person , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    
    
class Comments(models.Model):
    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(Person , on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics , on_delete=models.CASCADE)
    ratings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Location(models.Model):
    lat = models.IntegerField()
    lon = models.IntegerField()
    user = models.ForeignKey(Person , on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics , on_delete=models.CASCADE , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
