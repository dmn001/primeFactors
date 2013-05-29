import unittest
from primeFactors import primeFactors
 
class primeFactorsTest(unittest.TestCase):

   def setUp(self):
      self.p = primeFactors()

   def test_testOne(self):
      self.assertEqual([], self.p.generate(1))

   def test_testTwo(self):
      self.assertEqual([2], self.p.generate(2))

   def test_testThree(self):
      self.assertEqual([3], self.p.generate(3))

if __name__ == "__main__":
	unittest.main()
