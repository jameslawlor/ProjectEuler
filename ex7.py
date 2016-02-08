def primeList(i,list):
	if i not in list:
		for j in list:
			if i % j == 0:
				return
		list.append(i)

j = 3
list = [2]
while len(list) < 10001:
	primeList(j,list)
	j += 2

print list[-1]
