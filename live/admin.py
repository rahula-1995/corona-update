from django.contrib import admin

# Register your models here.
from .models import Report,State,District,Country,headWorld,headIndia
admin.site.register(Report)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(headWorld)
admin.site.register(headIndia)
