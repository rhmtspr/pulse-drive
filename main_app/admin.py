from django.contrib import admin
from .models import Car, Transaction

# Register your models here.
admin.site.register(Car)
admin.site.register(Transaction)