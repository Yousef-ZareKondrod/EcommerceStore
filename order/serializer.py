from rest_framework import serializers

from order.models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='account:customer_detail', read_only=True)
    item = serializers.HyperlinkedRelatedField(view_name='order:orderitem_detail', read_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(view_name='order:order_detail', read_only=True)
    product = serializers.HyperlinkedRelatedField(view_name='product:product_detail', read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'
