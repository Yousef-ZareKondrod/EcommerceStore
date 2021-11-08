from django.test import TestCase

# Create your tests here.
from customer.models import UserBase
from order.models import Order, OrderItem
from product.models import Category, Product


class TestOrderModel(TestCase):
    def setUp(self) -> None:
        UserBase.objects.create(email='yousef.zare2000@gmail.com')

        self.data1 = Order.objects.create(user_id='1',
                                          total_paid=500000,
                                          billing_status=True)

    def test_order_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Order))

    def test_order_model_entry2(self):
        data = self.data1.total_paid
        self.assertEqual(data, 500000)


class TestOrderItemModel(TestCase):
    def setUp(self) -> None:
        UserBase.objects.create(email='yousef.zare2000@gmail.com')
        Order.objects.create(user_id='1',
                             total_paid=500000,
                             billing_status=True)
        Category.objects.create(name='django', slug='django')

        Product.objects.create(category_id=1, title='django', created_by_id=1,
                               slug='django', price='500000', image='django')
        self.data1 = OrderItem.objects.create(order_id='1',
                                              product_id='1',
                                              price=500000,
                                              )


    def test_order_item_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, OrderItem))


    def test_order_model_entry2(self):
        data = self.data1.price
        self.assertEqual(data, 500000)
