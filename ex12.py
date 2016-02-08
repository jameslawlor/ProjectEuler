import math
def divCheck(x):
	if x % 2 != 0 or x%3 != 0 or x%5 != 0 or x%7!=0: 
		return
	noDiv = 1
	for i in range(1, int(math.ceil(math.sqrt(x)))+1):
		if x % i == 0: noDiv += 1;
	print x , noDiv*2
	return noDiv*2

x = 1 ; y = 1

while divCheck(x) < 500: 
	y += 1
	x += y
#print x, divCheck(x)
