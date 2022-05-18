from decimal import Decimal

from django.test import TestCase

from fakecandelfood.product import models as pmodels


class ProductTests(TestCase):

    def setUp(self) -> None:
        # Categories
        self.pizza_category = pmodels.Category.objects.create(title='Pizza')
        # Tags
        self.pizza_tag = pmodels.Tag.objects.create(title='Pizza')
        self.american_pizza = pmodels.Tag.objects.create(title='American pizza')
        # Products
        self.product = pmodels.Product.objects.create(
            title='Pizza itallian',
            price=Decimal(65000),
            category=self.pizza_category,
            description='Pizza itallian is the best pizza in the world'
        )
        self.product.tags.add(self.pizza_tag)
    
    def test_product_content(self) -> None:
        """
        Testing initial product content
        """
        self.assertEqual(pmodels.Product.objects.count(), 1)
        self.assertEqual(self.product.title, 'Pizza itallian')
        self.assertEqual(self.product.slug, 'pizza-itallian')
        self.assertEqual(self.product.category, self.pizza_category)
        self.assertEqual(self.product.tags.count(), 1)
        self.assertEqual(self.product.description, 'Pizza itallian is the best pizza in the world')
        self.assertEqual(self.product.price, 65000)
        self.assertEqual(self.product.comma_price, '65,000')
        self.assertEqual(self.product.price_as_toman, 65000)
        self.assertTrue(self.product.is_active)
        self.assertTrue(self.product.is_take_away)
        self.assertTrue(self.product.can_take_away())
    
    def test_create_product(self) -> None:
        """
        Testing creating product
        """
        new_product = pmodels.Product.objects.create(
            title='Pizza American',
            price=Decimal(80000),
            category=self.pizza_category,
            description='Pizza American is the best pizza in the world'
        )
        new_product.tags.add(self.pizza_tag, self.american_pizza)

        # Test
        self.assertEqual(pmodels.Product.objects.count(), 2)
        self.assertEqual(new_product.title, 'Pizza American')
        self.assertEqual(new_product.slug, 'pizza-american')
        self.assertEqual(new_product.category, self.pizza_category)
        self.assertEqual(new_product.tags.count(), 2)
        self.assertEqual(new_product.description, 'Pizza American is the best pizza in the world')
        self.assertEqual(new_product.price, 80000)
        self.assertEqual(new_product.comma_price, '80,000')
        self.assertEqual(new_product.price_as_toman, 80000)
        self.assertTrue(new_product.is_active)
        self.assertTrue(new_product.is_take_away)
        self.assertTrue(new_product.can_take_away())

    
    def test_delete_product(self) -> None:
        """
        Testing deleting a product
        """
        self.product.delete()
        self.assertEqual(pmodels.Product.objects.count(), 0)
    
    def test_update_product(self) -> None:
        """
        Testing updating a product
        """
        self.product.title = 'Pizza italian just for you'
        self.product.is_take_away = False
        self.product.save()

        self.assertEqual(self.product.slug, 'pizza-italian-just-for-you')
        self.assertFalse(self.product.can_take_away())