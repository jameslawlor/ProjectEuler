#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def palindromeCheck(input):
    for i in range(len(str(input))):
		if str(input)[i] != str(input)[-1-i]:
			return False
	return True

largest = 0.0

for a in range(999,100,-1):
	for b in range(999,100,-1):
		if palindromeCheck(a*b) == True and a*b > largest:
			largest = a*b

print largest			
