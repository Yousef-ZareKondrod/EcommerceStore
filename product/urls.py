from django.urls import path
from . import api

from . import views

app_name = 'product'
urlpatterns = [
    path('', views.products_all, name='products_all'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),

    path('api/productlist', api.ProductList.as_view()),
    path('api/productcreate', api.ProductCreateList.as_view()),
    path('api/productdetail/<int:pk>', api.ProductDetail.as_view(), name='product_detail')
]
