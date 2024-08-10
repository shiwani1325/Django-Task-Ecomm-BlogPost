from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ProductForm()

    return render(request, 'form.html', {'form': form})


def home(request):
    products=Product.objects.all()
    return render(request,'base.html', {'products': products})



