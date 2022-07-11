from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand, Car

# Create your views here.
def index(request):
    return render(request, 'cars_and_brands/index.html')

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

def cars(request, brand_id):
    data = []
    cars = Car.objects.all()
    for car in cars:
        if car.brand.id == brand_id:
            print(car.brand.name)
            data.append({'name': car.name, 'id': car.id, 'brand': car.brand.name, 'brand_id': car.brand.id})
    # print(cars)
    return render(request, 'cars_and_brands/cars.html', {'data': data})

def cars_id(request, brand_id, car_id):
    car = Car.objects.get(id=car_id)
    data = {'name': car.name, 'id': car.id}
    return render(request, 'cars_and_brands/car_id.html', data)