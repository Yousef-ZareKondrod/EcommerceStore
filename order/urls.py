from django.urls import path

from order import views, api

app_name = 'order'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('api/ordercreatelist', api.OrderCreateList.as_view(), name='order_createlist'),
    path('api/orderdetail/<int:pk>', api.OrderDetail.as_view(), name='order_detail'),
    path('api/orderitemcreatelist', api.OrderItemCreateList.as_view(), name='orderitem_createlist'),
    path('api/orderitemdetail/<int:pk>', api.OrderItemDetail.as_view(), name='orderitem_detail'),
]
