from django.db import models

# 1. AL-TAJ HAIR OIL Ka Model (Dukaan ka item)
class Product(models.Model):
    name = models.CharField(max_length=200, default="AL-TAJ HAIR OIL")
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

# 2. Customer Ke Order Ka Model (Khata)
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15) # WhatsApp rabtay ke liye
    address = models.TextField()
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=50, default='Pending') # Pending ya Delivered
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name} ({self.phone})"