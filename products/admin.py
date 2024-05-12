from django.contrib import admin

from products.models import Category, Promotion, Products

admin.site.register(Category)
admin.site.register(Promotion)
admin.site.register(Products)
