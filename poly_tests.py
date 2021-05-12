import unittest
import poly

class TestPoly(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test1(self):
        self.assertListAlmostEqual([1,2],[1,2])

    def test_add(self):
        poly1 = [2.3, 4.7, 1.0]
        poly2 = [1.2, 2.1, -3.2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])
    def test_add1(self):
        poly1 = [1, 3.4, 7.8]
        poly2 = [2.0, 5.6, 0.9]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.0, 9.0, 8.7])

    def test_mult(self):
        poly1 = [2, 3, 4]
        poly2 = [5, 6, 7]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [28, 45, 52, 27, 10])
    def test_mult1(self):
        poly1 = [1.2, 2.3, 3.4]
        poly2 = [4.5, 5.6, 6.7]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [22.78, 34.45, 36.22, 17.07, 5.4])

if __name__ == '__main__':
    unittest.main()