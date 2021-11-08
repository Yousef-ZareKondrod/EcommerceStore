from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from customer.models import UserBase
from customer.permissions import IsSuperUserOrOwner
from customer.serializer import CustomerSerializer


class CustomerCreateList(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = UserBase.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]


class CustomerDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = UserBase.objects.all()
    permission_classes = [
        IsSuperUserOrOwner
    ]