import random
from rsa_util import mod_inverse
from rsa_util import is_prime

#The encryption exponent, e
#Do not change this value
e = 65537

def RSAKeygen(bitlen):

	n = 0
	d = 0
	
	while n == 0:
		x = random.getrandbits(bitlen)
		if x % 2 == 1:
			n = x

	while d == 0:
		y = random.getrandbits(bitlen)
		if y % 2 == 1:
			d = y

	return n,d

def RSAEncrypt(n,m):
	c = m
	#Code goes here
	return c

def RSADecrypt(n,d,c):
	m = c
	#Code goes here
	return m

