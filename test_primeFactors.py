import unittest
from primeFactors import primeFactors
 
class primeFactorsTest(unittest.TestCase):

   def setUp(self):
      self.p = primeFactors()

   def test_generate_returns_list(self):
      self.assertEqual([], self.p.generate(1))

if __name__ == "__main__":
	unittest.main()
