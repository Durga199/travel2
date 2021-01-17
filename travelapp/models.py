from django.db import models
from django.contrib.auth.models import User

class travell(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()

    def __str__(self):
            return self.name

class blog(models.Model):
    bimg = models.ImageField(upload_to = 'pics')
    date = models.DateField()
    post = models.CharField(max_length=100)
    bname = models.CharField(max_length=100)
    bdesc = models.TextField()

# Create your models here.
    def __str__(self):
         return self.bname

class register(models.Model):
    username = models.CharField(max_length=200)
    dob=models.DateField()
    mobile=models.CharField(max_length=20)
    address=models.TextField()
    gender =models.CharField(max_length=20)
    nationality  =models.CharField(max_length=50)
    image = models.FileField(upload_to='pics/', null=True)

    def __str__(self):
        return self.username
