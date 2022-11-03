from unicodedata import category, name
from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def product(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "products.html", {'products':products, 'categories':categories})





def category(request, category_id):
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(categories=category)
        categories = Category.objects.all()
        return render(request, "category.html", {'category':category, 'products':products, 'categories':categories})
