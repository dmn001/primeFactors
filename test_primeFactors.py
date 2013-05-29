import unittest
from primeFactors import primeFactors
 
class primeFactorsTest(unittest.TestCase):

   def setUp(self):
      self.p = primeFactors()

   def test_0(self):
      pass

if __name__ == "__main__":
	unittest.main()
