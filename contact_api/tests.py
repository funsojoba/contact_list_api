from django.test import TestCase


class TestCi(TestCase):
    def test_sum(self):
        self.assertEqual((2 + 3), 5)
