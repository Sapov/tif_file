from django.test import TestCase
from django.urls import reverse
from printbanner.files.models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(text='jast text')

    def test_text_content(self):
        product = Product.objects.get(id=1)
        expexted_object_name = f'{product.text}'
        self.assertEqual(expexted_object_name, 'jast text')


class AccountViewTest(TestCase):

    def setUp(self):
        Product.objects.create(text='this is jast text')

    def test_view_url(self):
        resp = self.client.get('login/')
        self.assertEqual(resp.status_code, 200)

    def test_url_by_name(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_templates(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'login.html')





