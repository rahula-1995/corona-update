from django.db import models

# Create your models here.

class Report(models.Model):
    name= models.CharField(max_length=300,default="")
    mobile=  models.IntegerField( default=10)
    suspectm= models.IntegerField( default=10)
    suspectname=models.CharField(max_length=300, default="")
    suspectadress=models.CharField(max_length=1000, default="")