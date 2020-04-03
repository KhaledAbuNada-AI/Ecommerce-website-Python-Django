from . import views
from django.urls import path

app_name = 'product'
urlpatterns = [

    path('', views.product_list),
    path('<slug:slug>', views.product_detail, name='product_detail'),

]