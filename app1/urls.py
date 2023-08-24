
from django.urls import path
from app1.views import *

urlpatterns = [
    path('data/',data),
    path('login/',login, name="login"),
    path('',index),
    path('all-product/',allproduct,name="proall"),
    path('filter-product/<int:id>/',filterproduct,name="productfilter")
]