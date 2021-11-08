from importlib import import_module
from unittest import skip

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from product.models import Category, Product
from product.views import products_all

# Create your tests here.


class TestViewResponse(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='yousef.zare2000')
        Product.objects.create(category_id=1, title='django', created_by_id=1,
                               slug='django', price='20000', image='django')

    def test_url_allowed_hosts(self):
        """
        Testing allowed hosts
        :return:
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        # TODO: at the end enter your host for testing
        response = self.c.get('/', HTTP_HOST='Test.com')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Testing product response status
        :return:
        """
        response = self.c.get(reverse('product:product_detail', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Testing category response status
        :return:
        """
        response = self.c.get(reverse('product:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Testing homepage
        :param self:
        :return:
        """
        request = HttpRequest
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = products_all(request)
        html = response.content.decode('utf8')
        # print(html)
        self.assertIn('<title>Store</title>', html)
        self.assertEqual(response.status_code, 200)

