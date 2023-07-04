from django.contrib import admin
from .models import Product,contacted_user

# Register your models here.

admin.site.register(Product)
admin.site.register(contacted_user)