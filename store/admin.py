from django.contrib import admin
from .models import Product, Order

# Admin panel mein in dono ko show karwao
admin.site.register(Product)
admin.site.register(Order)