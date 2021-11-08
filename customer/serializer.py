from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from customer.models import UserBase
from product.models import Product


class CustomerSerializer(serializers.ModelSerializer):
    country = CountryField()
    class Meta:
        model = UserBase
        fields = '__all__'




