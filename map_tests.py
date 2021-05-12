import unittest
import map

class TestCases(unittest.TestCase):
   def test_1(self):
      a = [1, 2, 3]
      b = map.square_all(a)
      self.assertListEqual(b, [1, 4, 9])
   def test_2(self):
      a = [10, 2, 5 ,6]
      b = map.square_all(a)
      self.assertListEqual(b, [100, 4, 25, 36])
 
   def test_3(self):
      a = [1, 2, 3]
      b = map.add_n_all(a, 1.3)
      self.assertListEqual(b, [2.3, 3.3, 4.3])
   def test_4(self):
      a = [10, 2, 5 ,6]
      b = map.add_n_all(a, 5)
      self.assertListEqual(b, [15, 7, 10, 11])
 
   def test_5(self):
      a = [1, 2, 3]
      b = map.even_or_odd_all(a)
      self.assertListEqual(b, [False, True, False])
   def test_6(self):
      a = [10, 2, 5 ,6]
      b = map.even_or_odd_all(a)
      self.assertListEqual(b, [True, True, False, True])



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

#