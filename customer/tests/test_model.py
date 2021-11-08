from django.test import TestCase

# Create your tests here.
from customer.models import *


class TestUserModel(TestCase):

    def setUp(self):
        self.data1 = UserBase.objects.create(email='yousef.zare2000@gmail.com',
                                             user_name='yousef.zare2000',
                                             first_name='yousef',
                                             last_name='zare',
                                             country='iran',
                                             phone_number='9123456789',
                                             postcode='1234567890',
                                             address_line_1='a',
                                             address_line_2='b',
                                             town_city='tabriz',
                                             is_active=True,
                                             is_staff=True)

    def test_category_model_entry(self):
        """
        Testing User model data insertion/types/field attributes
        :return:
        """
        data = self.data1
        self.assertTrue(isinstance(data, UserBase))

    def test_category_model_entry2(self):
        """
        Testing user model default email
        :return:
        """
        data = self.data1.email
        self.assertEqual(str(data), 'yousef.zare2000@gmail.com')

    def test_category_model_entry3(self):
        """
        Testing user model default username
        :return:
        """
        data = self.data1.user_name
        self.assertEqual(str(data), 'yousef.zare2000')

    def test_category_model_entry4(self):
        """
        Testing user model default firstname
        :return:
        """
        data = self.data1.first_name
        self.assertEqual(str(data), 'yousef')

    def test_category_model_entry5(self):
        """
        Testing user model default lastname
        :return:
        """
        data = self.data1.last_name
        self.assertEqual(str(data), 'zare')

    def test_category_model_entry6(self):
        """
        Testing user model default country
        :return:
        """
        data = self.data1.country
        self.assertEqual(str(data), 'iran')

    def test_category_model_entry7(self):
        """
        Testing user model default phone number
        :return:
        """
        data = self.data1.phone_number
        self.assertEqual(str(data), '9123456789')

    def test_category_model_entry8(self):
        """
        Testing user model default postcode
        :return:
        """
        data = self.data1.postcode
        self.assertEqual(str(data), '1234567890')


    def test_category_model_entry9(self):
        """
        Testing user model default address
        :return:
        """
        data1 = self.data1.address_line_1
        self.assertEqual(str(data1), 'a')
        data2 = self.data1.address_line_2
        self.assertEqual(str(data2), 'b')

    def test_category_model_entry10(self):
        """
        Testing user model default city
        :return:
        """
        data = self.data1.town_city
        self.assertEqual(str(data), 'tabriz')

    def test_category_model_entry11(self):
        """
        Testing user model default is_active
        :return:
        """
        data = self.data1.is_active
        self.assertEqual(str(data), 'True')

    def test_category_model_entry12(self):
        """
        Testing user model default is_staff
        :return:
        """
        data = self.data1.is_staff
        self.assertEqual(str(data), 'True')



