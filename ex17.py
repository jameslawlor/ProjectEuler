def arrCon(y):
	return [int(x) for x in str(y)]

number = 100

s = 0

dic = { 1 : 'one' , 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',11:'eleven',
12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen', 17:'seventeen',18:'eighteen', 19:'nineteen',
20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

for number in xrange(1,1000):
	if number < 20: # 
		s += len(dic[ number ])
	elif number >= 20 and number < 100:
		number = arrCon(number)
		if number[-1] == 0:
			s += len(dic[ int(str(number[0])+str(0))])
		else:
			s += len(dic[ int(str(number[0])+str(0))]) + len(dic[number[-1]])
	elif number >= 100 and number < 1000:
		number = arrCon(number)
		if number[-1] == 0 and number[-2] == 0:
			s += len(dic[number[0]] + 'hundred')
		elif number[-1] == 0 and number[-2] != 0:
			s += len(dic[number[0]] + 'hundredand') + len(dic[ int( str(number[-2]) + str(0)  )])
		else:
			if number[-2] == 0:
				s += len(dic[number[0]] + 'hundredand')  + len(dic[number[-1]])
			elif number[-2] == 1:
				s += len(dic[number[0]] + 'hundredand') + len( dic[ 10*int(number[-2]) + number[-1]]) 
			else:
				s += len(dic[number[0]] + 'hundredand') + len(dic[int(str(number[1]) + str(0))]) + len(dic[number[-1]])

		
	print number , s

print s + len('onethousand')

