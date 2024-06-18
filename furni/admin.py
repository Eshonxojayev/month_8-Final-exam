from django.contrib import admin
from .models import Stol, Stul, Creslo, Product
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Stol)
class StolAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug':('title',)}
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'id')
    ordering = ('id',)


@admin.register(Stul)
class StulAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'title')
    # prepopulated_fields = {'slug':('title',)}
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'id')
    ordering = ('id',)

@admin.register(Creslo)
class CresloAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug':('title',)}
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'id')
    ordering = ('id',)

@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'description_obj', 'price')
    list_display_links = ('id', 'name', 'description_obj', 'price')
    search_fields = ('name', 'id')
    ordering = ('id',)
    def description_obj(self, obj):
        return obj.description[:5]