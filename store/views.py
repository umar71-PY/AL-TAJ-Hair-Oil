from django.shortcuts import render, redirect
from .models import Product, Order
from django.contrib import messages

def home(request):
    product = Product.objects.first() 
    
    if request.method == 'POST':
        c_name = request.POST.get('name')
        c_phone = request.POST.get('phone')
        c_address = request.POST.get('address')
        
        # New fields from our VIP JS Cart
        c_cart = request.POST.get('cart_summary') 
        c_payment = request.POST.get('payment_method')

        # The Master Hack: Sab data ko Address field mein combine kar do
        full_order_details = f"ADDRESS: {c_address} \n\n[PAYMENT METHOD]: {c_payment} \n[CART DETAILS]: {c_cart}"
        
        Order.objects.create(
            customer_name=c_name,
            phone=c_phone,
            address=full_order_details,
            quantity=1 # Default value taake DB error na de
        )
        
        messages.success(request, 'Thank you for your order! We will send your tracking ID to your WhatsApp number once your order is dispatched.')
        return redirect('home')
        
    return render(request, 'index.html', {'product': product})