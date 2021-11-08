from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from order.permissions import IsSuperUserOrOwner
from order.permissions import IsSuperUserOrOwnerItem
from order.serializer import *


class OrderCreateList(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]


class OrderDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [
        IsSuperUserOrOwner
    ]


class OrderItemCreateList(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]


class OrderItemDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [
        IsSuperUserOrOwnerItem
    ]
