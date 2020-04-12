from rest_framework import serializers
from .models import State,District,Country,headWorld,headIndia

class Countrysearializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=('country_name','country_case','country_active_case','country_recovered_case','country_death_case')

class Statesearializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields=('state_name','state_case','state_active_case','state_recovered_case','state_death_case')

class Districtsearializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields=('district_name','district_cases')

class headWorldsearializer(serializers.ModelSerializer):
    class Meta:
        model=headWorld
        fields=('confirmed_world_case','active_world_case','world_death_case','recovered_world_case')

class headindiasearializer(serializers.ModelSerializer):
    class Meta:
        model=headIndia
        fields=('confirmed_india_case','active_india_case','india_death_case','recovered_india_case')