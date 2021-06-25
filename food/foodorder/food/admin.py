from django.contrib import admin
from .models import Category, Product


# Register your models here.

class C_Admin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, C_Admin)


class P_Admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available', ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, P_Admin)
