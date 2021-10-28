def mymethod(integer):
	if integer>5 and integer<2000:
		result = 0
		numbers = []
		results = []
		for i in range(1,integer+1):
			if i%2 == 0:
				numbers.append(i)
				result = i*i
				results.append(result)
	return numbers, results 

b,c = mymethod(6)

count = len(b)
for i in range(0,count):
	print ('%d^2 = %d' %(b[i],c[i]))


