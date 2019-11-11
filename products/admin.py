from django.contrib import admin
from .models import Product, Category, Offer

class CategoryAdmin(admin.ModelAdmin):
    pass

class OfferAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Offer, OfferAdmin)
