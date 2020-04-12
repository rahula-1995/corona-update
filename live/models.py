from django.db import models

# Create your models here.

class Report(models.Model):
    informer_name= models.CharField(max_length=300,default="")
    informer_mobile=  models.CharField(max_length=11,default="")
    suspect_mobile= models.CharField( max_length=11,default="")
    suspect_name=models.CharField(max_length=300, default="")
    suspect_adress=models.CharField(max_length=1000, default="")
    def __str__(self):
        return self.informer_name

