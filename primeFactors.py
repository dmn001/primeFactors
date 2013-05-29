class primeFactors(object):
	def __init__(self):
		self.__primes = []

	def generate(self,n):
		candidate = 2
		while n > 1:
			while n % candidate == 0:
				self.__primes.append(candidate)
				n /= candidate
			candidate += 1
		return self.__primes
