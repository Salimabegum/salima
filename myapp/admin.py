from django.contrib import admin

# Register your models here.

from .models import Product_field,user_field,buyed

admin.site.register(Product_field)
admin.site.register(user_field)
admin.site.register(buyed)
