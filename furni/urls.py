from django.urls import path, include
from furni import views

urlpatterns = [
    path('stol/', views.stol, name='stol'),
    path('stul/', views.stul, name='stul'),
    path('creslo/', views.creslo, name='creslo'),
    path('product/', views.product, name='product'),
]