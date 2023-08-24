from django.contrib import admin
from app1.models import Userregister,Category
# Register your models here.

class userdisplay(admin.ModelAdmin):
    list_display=['id','name','email','number','address']
    list_filter=['name','email','number']
    search_fields=['name','number']
admin.site.register(Userregister,userdisplay)


admin.site.register(Category)



