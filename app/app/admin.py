from django.contrib import admin

from app.models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')


@admin.register(ProductInfo)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Parameter)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)
class CategoryAdmin(admin.ModelAdmin):
    pass