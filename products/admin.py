from django.contrib import admin
from .models import Users, Products

admin.site.register([Users, Products])