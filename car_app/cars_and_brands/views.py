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
        data.append({'name': brand.name, 'id': brand.id})
    print(data)
    return render(request, 'cars_and_brands/brands.html', {'data': data})

def brands_id(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    data = {'name': brand.name, 'id': brand_id}
    return render(request, 'cars_and_brands/brands_id.html', data)