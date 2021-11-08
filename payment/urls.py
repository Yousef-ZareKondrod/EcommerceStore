from django.urls import path

from payment import views

app_name = 'payment'

urlpatterns = [
    path('', views.CartView, name='Cart'),
    path('orderplaced/', views.order_placed, name='order_placed'),
    path('error/', views.Error.as_view(), name='error'),
    # url(r'^request/$', views.send_request, name='request'),
]
