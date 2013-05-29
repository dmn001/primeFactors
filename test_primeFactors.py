import unittest
from primeFactors import primeFactors
 
class primeFactorsTest(unittest.TestCase):

	def setUp(self):
		self.p = primeFactors()

	def test_One(self):
		self.assertEqual([], self.p.generate(1))

	def test_Two(self):
		self.assertEqual([2], self.p.generate(2))

	def test_Three(self):
		self.assertEqual([3], self.p.generate(3))

	def test_Four(self):
		self.assertEqual([2,2], self.p.generate(4))

	def test_Six(self):
		self.assertEqual([2,3], self.p.generate(6))

	def test_Eight(self):
		self.assertEqual([2,2,2], self.p.generate(8))

if __name__ == "__main__":
	unittest.main()
