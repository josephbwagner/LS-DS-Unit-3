import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    '''Making sure Acme products are the tops!'''

    def test_default_product_price(self):
        '''Test default product price being 10.'''
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        '''Test default product flammability being 0.5'''
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_product_stealability(self):
        '''
        Test product stealability being 'Very stealable!' when price > weight
        '''
        prod = Product('Test Product', price=20, weight=2)
        self.assertEqual(prod.stealability(), 'Very stealable!')


class AcmeReportTests(unittest.TestCase):
    '''Making sure Acme reports ROCK!'''

    def test_default_num_products(self):
        '''Test product list length'''
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        '''Test generated product names for compliance with English grammar'''
        products = generate_products()
        name_list = [item.name.split(' ', 1) for item in products]
        for name in name_list:
            self.assertIn(name[0], ADJECTIVES)
            self.assertIn(name[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
