from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from product.models import Category, Product


class TestCartView(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='yousef.zare2000')
        Product.objects.create(category_id=1, title='django1', created_by_id=1,
                               slug='django1', price='20000', image='django')
        Product.objects.create(category_id=1, title='django2', created_by_id=1,
                               slug='django2', price='20000', image='django')
        Product.objects.create(category_id=1, title='django3', created_by_id=1,
                               slug='django3', price='20000', image='django')

        self.client.post(
            reverse('cart:cart_add'), {'productid': 1, 'productqty': 1, 'action': 'post'}, xhr=True
        )
        self.client.post(
            reverse('cart:cart_add'), {'productid': 2, 'productqty': 2, 'action': 'post'}, xhr=True
        )

    def test_cart_url(self):
        """
        Testing homepage response status
        :return:
        """
        response = self.client.get(reverse('cart:cart_summary'))
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        """
        Testing adding items to the cart
        :param self:
        :return:
        """

        response = self.client.post(
            reverse('cart:cart_add'), {'productid': 3, 'productqty': 1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('cart:cart_add'), {'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 3})

    def test_cart_delete(self):
        """
        Testing deleting item from the cart
        :return:
        """
        response = self.client.post(
            reverse('cart:cart_delete'), {'productid': 2, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': 20000})

    def test_cart_update(self):
        """
        Testing updating item from the cart
        :return:
        """
        response = self.client.post(
            reverse('cart:cart_update'), {'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': 40000})
