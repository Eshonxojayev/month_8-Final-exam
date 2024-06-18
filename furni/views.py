from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Stol, Stul, Creslo, Product


class HomePageView(View):
    def get(self, request):
        stul = Stul.objects.order_by('-name')[:3]
        stol = Stol.objects.order_by('title')[:3]
        creslo = Creslo.objects.all()
        context = {
            'stul': Stul,
            'stol': Stol,
            'creslo': Creslo
        }
        return render(request, "index.html", context)


class ShopPageView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'shop.html', context)


class AboutPAgeView(View):
    def get(self, request):
        return render(request, 'about.html')


class ServicePageView(View):
    def get(self, request):
        return render(request, 'services.html')


class BlogPageView(View):
    def get(self, request):
        return render(request, 'blog.html')


class ContactPageView(View):
    def get(self, request):
        return render(request, 'contact.html')