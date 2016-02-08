def f(y):
	length = 1
	while y != 1:
		if y%2 == 0: y = y/2
		else: y = y*3 + 1
		length += 1		

	return length

#print f(13)

longest = 0 
for x in xrange(2,1000000): 
	if f(x) > longest:
		longest = f(x)
		print x
