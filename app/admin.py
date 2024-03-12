from django.contrib import admin
from .models import Product , Customer
admin.site.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount_price','category','product_image']

    

admin.site.register((Customer))
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city', 'state', 'zipcode']
# Register your models here.
