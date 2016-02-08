array = []

with open('ex67.txt') as f:
	for line in f.readlines():
		array.append([ int(x) for x in line.split() ])

for i in range(len(array)-2,-1,-1):
	for j in range(len(array[i])):	# Starting at the second from bottom row we iterate through, row by row. Each element has added to it the larger value of its two downstairs neighbours
		array[i][j] += max([array[i+1][j] , array[i+1][j+1]  ])

print array[0][0]
