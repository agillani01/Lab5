import unittest
import filter

class TestCases(unittest.TestCase):
   def test_1(self):
      a = [1, 2, 3]
      b = filter.are_positive(a)
      self.assertListEqual(b, [2])
   def test_2(self):
      a = [4, 4, 4, 6, 11, 15, 8]
      b = filter.are_positive(a)
      self.assertListEqual(b, [4, 4, 4, 6, 8])

   def test_3(self):
      a = [1, 2, 3]
      b = filter.are_greater_than_n(a, 4)
      self.assertListEqual(b, [])
   def test_4(self):
      a = [8, 10, 4, 1, 100]
      b = filter.are_greater_than_n(a, 4)
      self.assertListEqual(b, [8, 10, 100])

   def test_5(self):
      a = [1, 2, 3]
      b = filter.are_divisible_by_n(a, 2)
      self.assertListEqual(b, [2])
   def test_6(self):
      a = [8, 10, 25, 1, 100]
      b = filter.are_divisible_by_n(a, 5)
      self.assertListEqual(b, [10, 25, 100])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()