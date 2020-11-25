from django.shortcuts import render

def main(request):
    context = {}
    return render(request, 'store/main.html')

def order(request):
    context = {}
    return render(request, 'store/order.html')

def cart(request):
    context = {}
    return render(request, 'store/cart.html') 

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html') 