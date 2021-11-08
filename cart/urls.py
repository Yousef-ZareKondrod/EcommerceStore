from django.urls import path

from cart import views

app_name = 'card'
urlpatterns = [
    path('', views.card_summary, name='card_summary'),
    path('add/', views.card_add, name='card_add'),
    path('delete/', views.card_delete, name='card_delete'),
    path('update/', views.card_update, name='card_update'),
]
