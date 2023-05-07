from django.test import TestCase
from django.urls import reverse
from . models import Product


# class ProductModelTest(TestCase):
#     def setUp(self):
#         Product.objects.create(quantity=1000)
#
#     def test_text_content(self):
#         product = Product.objects.get(id=1)
#         exprected_object_name = f'{product.text}'
#         self.assertEqual(exprected_object_name, 1000)


class HomePageViewTest(TestCase):

    def setUp(self):
        Product.objects.create(quantity=1, )

    def test_view_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    # def test_url_by_name(self):
    #     resp = self.client.get(reverse('home'))
    #     self.assertEqual(resp.status_code, 200)
    #
    # def test_view_uses_correct_templates(self):
    #     resp = self.client.get(reverse('home'))
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertTemplateUsed(resp, 'index.html')
    #




