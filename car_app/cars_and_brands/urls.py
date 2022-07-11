from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('brands/', views.brands),
    path('brands/<int:brand_id>/', views.brands_id),
]