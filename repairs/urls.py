from django.urls import path
from . import views

urlpatterns = [
    path('vehicle/', views.vehicle_select, name='vehicle_select'),
    path('instructions/<str:vehicle>/<str:repair>/', views.repair_instructions, name='repair_instructions'),
]
