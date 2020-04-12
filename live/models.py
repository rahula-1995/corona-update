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

class Country(models.Model):
    country_name= models.CharField(max_length=300,default="")
    country_case= models.CharField(max_length=300,default="")
    country_active_case= models.CharField(max_length=300,default="")
    country_recovered_case = models.CharField(max_length=300, default="")
    country_death_case= models.CharField(max_length=300,default="")

    def __str__(self):
        return self.country_name

class State(models.Model):
    state_name= models.CharField(max_length=300,default="")
    state_case= models.CharField(max_length=300,default="")
    state_active_case= models.CharField(max_length=300,default="")
    state_recovered_case = models.CharField(max_length=300, default="")
    state_death_case= models.CharField(max_length=300,default="")

    def __str__(self):
        return self.state_name

class District(models.Model):
    district_name= models.CharField(max_length=300,default="")
    district_cases= models.CharField(max_length=300,default="")

    def __str__(self):
        return self.district_name

class headWorld(models.Model):

    confirmed_world_case= models.CharField(max_length=300,default="")
    active_world_case= models.CharField(max_length=300,default="")
    world_death_case= models.CharField(max_length=300,default="")
    recovered_world_case=models.CharField(max_length=300,default="")

    def __str__(self):
        return self.confirmed_world_case


class headIndia(models.Model):

    confirmed_india_case= models.CharField(max_length=300,default="")
    active_india_case= models.CharField(max_length=300,default="")
    india_death_case= models.CharField(max_length=300,default="")
    recovered_india_case=models.CharField(max_length=300,default="")

    def __str__(self):
        return self.confirmed_india_case