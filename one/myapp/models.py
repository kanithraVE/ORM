from django.db import models
from django.contrib import admin 
class service_DB(models.Model):
    name=models.CharField(max_length=20)
    phone_number=models.IntegerField(primary_key= True)
    license_number=models.CharField(max_length=10)
    issue=models.TextField()
    payment_method=models.CharField()
    date_of_arrival=models.DateField()
    exp_date_of_departure=models.DateField()
class service_DBAdmin(admin.ModelAdmin):
    list_display = ["name","phone_number","license_number","issue","payment_method","date_of_arrival","exp_date_of_departure"]

