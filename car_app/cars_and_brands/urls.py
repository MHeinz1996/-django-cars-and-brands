from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('brands/', views.brands),
    path('brands/<int:brand_id>/', views.brands_id),
    path('brands/<int:brand_id>/cars/', views.cars),
    path('brands/<int:brand_id>/cars/<int:car_id>/', views.cars_id),
]