def primeList(i, list):
	
	if i not in list:	# if i is not in our list we need to figure out if its prime or not
		for j in list:
			if i % j == 0:	# indicates not a prime
				return
		list.append(i)		# if i is not divisible by any number in our list it must be prime, so we append i to the list

	return

list = [2]
i = 3
while list[-1] < 2000000:
	primeList(i, list)	
	i += 2
#	print list[-1]

