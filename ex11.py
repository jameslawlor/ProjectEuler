with open('ex11.txt','r') as f: content = f.readlines() 
newArray = []
for line in content: newArray.append(map(int,line.split()))
l = 0
for i in range(len(newArray)-3):	# down
	for j in range(len(newArray)):
		if newArray[i][j]*newArray[i+1][j]*newArray[i+2][j]*newArray[i+3][j] > l:
			l = newArray[i][j]*newArray[i+1][j]*newArray[i+2][j]*newArray[i+3][j]
for i in range(len(newArray)):	# right
	for j in range(len(newArray)-3):
		if newArray[i][j]*newArray[i][j+1]*newArray[i][j+2]*newArray[i][j+3] > l:
			l = newArray[i][j]*newArray[i][j+1]*newArray[i][j+2]*newArray[i][j+3]

for i in range(len(newArray)-3):	# down right
	for j in range(len(newArray)-3):
		if newArray[i][j]*newArray[i+1][j+1]*newArray[i+2][j+2]*newArray[i+3][j+3] > l:
			l = newArray[i][j]*newArray[i+2][j+1]*newArray[i+2][j+2]*newArray[i+3][j+3]

for i in range(3,len(newArray)):	# up right
	for j in range(len(newArray)-3):
		if newArray[i][j]*newArray[i-1][j+1]*newArray[i-2][j+2]*newArray[i-3][j+3] > l:
			l = newArray[i][j]*newArray[i-1][j+1]*newArray[i-2][j+2]*newArray[i-3][j+3]
print l
