from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand, Car

# Create your views here.
def index(request):
    data = []
    brands = Brand.objects.all()
    for brand in brands:
        print(brand.name)
        data.append({'name': brand.name})
    print(data)
    return render(request, 'cars_and_brands/index.html', {'data': data})

def brands(request):
    data = []
    brands = Brand.objects.all()
    for brand in brands:
        print(brand.name)
        data.append({'name': brand.name})
    print(data)
    return render(request, 'cars_and_brands/brands.html', {'data': data})