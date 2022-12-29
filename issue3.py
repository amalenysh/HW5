from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_equal(self):
        transformed = fit_transform('hello', 'Amal')
        expected = [
            ('hello', [0, 1]),
            ('Amal', [1, 0])
        ]
        self.assertEqual(transformed, expected)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_doubles(self):
        transformed = fit_transform('hello', 'Amal', 'hello')
        expected = [
            ('hello', [0, 1]),
            ('Amal', [1, 0]),
            ('hello', [0, 1]),
        ]

        self.assertEqual(transformed, expected)

    def test_a_in_b(self):
        a = ('Amal', [0, 1])
        b = fit_transform('Amal', 'World')
        self.assertIn(a, b)
