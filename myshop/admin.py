from django.contrib import admin
from .models import Category,Product,MyImage

# Register your models here.

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','Pname','Price','Description']

admin.site.register(Product,ProductAdmin) 

class MyImageAdmin(admin.ModelAdmin):
    list_display=['name','description','myimage']

admin.site.register(MyImage,MyImageAdmin)   