"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc 

class calcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Adding numbers togeter"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)


    def test_subract_numbers(self):
        """Test to subract numbers"""
        res = calc.subract(10, 15)

        self.assertEqual(res, 5)