#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math

for a in range(1,500):
	for b in range(1,a):
		if a + b + math.sqrt(a*a + b*b) == 1000.0:
			print a*b*math.sqrt(a*a+b*b)
			stop

