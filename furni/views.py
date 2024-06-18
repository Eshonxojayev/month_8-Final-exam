from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from .models import Stol, Stul, Creslo, Product

class StolView(View):
    def post(self, request):
        name = request.POST('name')
        image = request.POST('image')
        title = request.POST("title")

        return render(name= name, image= image, title= title )

