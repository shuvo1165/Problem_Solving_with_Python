def mymethod(values):
	comment = []
	for i in range(len(values)):
		if values[i]>0:
			if values[i] %2 == 0:
				comment.append('EVEN POSITIVE')
			else:
				comment.append('ODD POSITIVE')
		elif values[i]<0:
			if values[i] %2 == 0:
				comment.append('EVEN NEGETIVE')
			else:
				comment.append('ODD NEGETIVE')
		else:
			comment.append('NULL')
	return comment



values = []

n = int(input('Total case:'))
for i in range(0,n):
	x=int(input('Enter value %d:'%i))
	values.append(x)
get = mymethod(values)
for i in range(len(get)):
	print('%s'%get[i])
