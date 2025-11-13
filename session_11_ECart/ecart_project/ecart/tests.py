from django.test import TestCase
from django.urls import reverse
from .models import Category, Product

class ProductViewTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Mobiles', slug='mobiles')
        self.product = Product.objects.create(
            name='Redmi 12',
            slug='redmi-12',
            price=10000,
            stock=5,
            category=self.category
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('ecart:home'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page(self):
        response = self.client.get(reverse('ecart:product_detail', args=['redmi-12']))
        self.assertContains(response, 'Redmi 12')

    def test_search_functionality(self):
        response = self.client.get(reverse('ecart:search') + '?q=Redmi')
        self.assertContains(response, 'Redmi 12')

