def mymethod(n,lengths,strings):
	u = 0
	i = 0
	l = 0
	result = []
	while i <n:
		j = 0
		count = 0
		while j < lengths[l]:
			s = strings[u]
			k = 0
			while k < len(s):
				ap = ord(s[k])-65
				ei = j
				pe = k

				count = count + ap + ei + pe
				k = k+1
			u = u+1
			j = j+1
		result.append(count)
		l = l+1
		i = i+1
	return result


lengths = []
strings = []
n = int(input('N:'))
i =1
while i <= n:
	l = int(input('L:'))
	lengths.append(l)
	j =1 
	while j<=l:
		string = str(input())
		strings.append(string)
		j = j+1
	i = i+1

ans = mymethod(n,lengths,strings)

for i in range(len(ans)):
	print(ans[i])




