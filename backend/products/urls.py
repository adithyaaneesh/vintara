from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.product_list,name='product-list'),
    path('products/<int:pk>/',views.product_detail,name='product-detail'),
    path('categories/',views.category_list,name='category-list'),
    path('categories/<int:pk>/',views.category_detail,name='category-detail'),
    path('product-images/',views.product_image_list,name='product-image-list'),
    path('product-images/<int:pk>/',views.product_image_delete,name='product-image-delete'),

]