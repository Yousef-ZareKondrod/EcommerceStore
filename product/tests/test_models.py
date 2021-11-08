from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from customer.models import UserBase
from product.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Testing category model data insertion/types/field attributes
        :return:
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry2(self):
        """
        Testing category model default name
        :return:
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        UserBase.objects.create(email='yousef.zare2000@gmail.com')
        self.data1 = Product.objects.create(category_id=1, title='django', created_by_id=1,
                                            slug='django', price='20000', image='django')

    def test_products_model_entry(self):
        """
        Testing products model data insertion/types/field attributes
        :return:
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))

    def test_products_model_entry2(self):
        """
        Testing products model default name
        :return:
        """
        data = self.data1
        self.assertEqual(str(data), 'django')