def mymethod(d,n):
	result= []
	k = len(d)
	i = 0
	while i < k:                           # continue the loop till the lenght of list
		if n[i].find(d[i]) != -1:          # finding desire values(which preserved in 'd[i]') from 'n[i]'. if not found than find() return -1.  
			temp = n[i].replace(d[i],'')   # replace the desire value from 'n[i]' with ''
			if temp == '':                 # after repaceing values with '', if the variable goes empty, must fill with a '0'
				temp = '0'
			temp = int(temp)
			result.append(temp)
		else:
			temp = int(n[i])               # if desire value not found in a string than it should remain the same!
			result.append(temp)
		i+=1
	return result



d = []
n = []
while (True):                                   # kind  a infinity loop!
	problem, string = map(str, input().split()) # catch multiple inputs at a glance
	if (problem == "0" and string == "0"):      # logic to get out from the loop
		break
	else:
		d.append(problem)
		n.append(string)


result = mymethod(d,n)

for i in range(len(result)):
	print(result[i])