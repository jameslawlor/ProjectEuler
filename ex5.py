#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisible(number):

		for i in range(20, 0,-1):
		if number % i != 0 :
			return False

	return True

j = 3

while divisible(j) != True:
	j+=1

print j
