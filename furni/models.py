from django.db import models
from .helpers import SaveMediaFiles, Choises
from django.contrib.auth.models import User

class Stol(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(verbose_name='Slug', max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.category_img_path)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Stul(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(verbose_name='Slug', max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.category_img_path)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Creslo(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(verbose_name='Slug', max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.category_img_path)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.product_img_path)
    price = models.FloatField()
    price_type = models.CharField(max_length=10, choices=Choises.PriceType.choices, default=Choises.PriceType.s)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
