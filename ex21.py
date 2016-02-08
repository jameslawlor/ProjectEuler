import math
def d(n):
	s = 0
	for i in xrange(1,int(n/2)+1):	
		if n % i == 0: s += i
	return s

def amicable(x , y):
	if d(x) == y and d(y) == x: return True
	else: return False

sum = 0
for x in xrange(1,10000):
	for y in xrange(1,10000):
		if amicable(x,y) == True: sum+= x + y
	print x
print sum/2
