from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView

from product.models import Product
from product.permissions import IsSuperUserOrNot
from product.serializer import ProductSerializer


class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreateList(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]


class ProductDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    permission_classes = [
        IsSuperUserOrNot
    ]
