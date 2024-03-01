from django.contrib import admin
from .models import Product
admin.site.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount_price','category','product_image']

    


# Register your models here.
