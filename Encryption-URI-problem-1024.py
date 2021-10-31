def mymethod(data):
	case = 0
	values = []
	while case < len(data): # Loop for number of cases
		s = data[case]
		i = 0
		strr = ''
		while i < len(s):   # loop run till the length of each strings tell
			if s[i].isalpha() == True: # 1st step: only swap values for Alphabetes
				temp = chr(ord(s[i]) + 3) # value swap 3 step to right
			else:
				temp = s[i]                # remain the none alphabet values same
			
			strr = strr+temp                # save each charecter as string 
			i+=1


		strr=strr[::-1]                      # 2nd step: reverse the modified string


		strr2 = ''
		k =0
		j = int(len(s)/2)

		while k < len(s):                    #3rd step: swap half of the modified string
			if k >= j:
				temp = chr(ord(strr[k]) - 1) # swap 1 step left
			else:
				temp = strr[k]

			strr2 = strr2+temp 
			k+=1

		values.append(strr2)                   # encrypted data saveing in a list 
		case+=1
	return values

data = []
n = int(input())                               # Number of case input
i = 1
while i <= n:
	line = str(input())                        # strings for encryption
	data.append(line)
	i = i+1

result = mymethod(data)
j =0
for j in range(len(result)):
	print(result[j])