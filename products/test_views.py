""" Testing the products.views.py"""

from django.test import TestCase


class TestViews(TestCase):
    """ Testing for Product Views"""

    def test_all_sarees(self):
        """ All Sarees page Testing """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_chiffon_sarees(self):
        """ Chiffon page Testing """
        response = self.client.get('/products/?category=chiffon_sarees')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html', '?category=chiffon_sarees')

    def test_cotton_sarees(self):
        """ Cotton Sarees page Testing """
        response = self.client.get('/products/?category=cotton_sarees')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html', '?category=cotton_sarees')

    def test_silk_sarees(self):
        """ Silk Sarees page Testing """
        response = self.client.get('/products/?category=silk_sarees')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html', '?category=silk_sarees')

    def test_by_price(self):
        """ Sort by price sarees page Testing """
        response = self.client.get('/products/?sort=price&direction=asc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html', '?sort=price&direction=asc')

    def test_by_rating(self):
        """ Sort by rating sarees page Testing """
        response = self.client.get('/products/?sort=rating&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html', '?sort=rating&direction=desc')

    def test_by_category(self):
        """ Sort by Category sarees page Testing """
        response = self.client.get('/products/?sort=category&direction=asc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html', '?sort=category&direction=asc')

    # def test_add_product_page(self):
    #     """ Test for add product """
    #     response = self.client.get('/add/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'products/add_product.html')
