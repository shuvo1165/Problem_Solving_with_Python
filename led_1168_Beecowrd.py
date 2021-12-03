def mymethod(digs):                    # get the numbers, need to findout, how many LED required to visualize the each numbers
	lenOfLi = len(digs)                 
	numOfLed = []
	i = 0
	while i<lenOfLi:
		temp = digs[i]                  # Put immediate value from list in a temporary space
		lenOfDig = len(temp)            # measure the lenth of the value initiate in temp space
		j = 0
		count = 0
		while j<lenOfDig:               # loop for analyse every digit in a number(here numbers in str form)
			if temp[j] == '1':          # The digit '1' needs two LED to visualize, '2' need five LED, '3' need...
				count +=2
			elif temp[j] == '2':
				count +=5
			elif temp[j] == '3':
				count +=5
			elif temp[j] == '4':
				count +=4
			elif temp[j] == '5':
				count +=5
			elif temp[j] == '6':
				count +=6
			elif temp[j] == '7':
				count +=3
			elif temp[j] == '8':
				count +=7
			elif temp[j] == '9':
				count +=6
			else:
				count +=6
			j+=1
		numOfLed.append(count)
		i+=1
	return numOfLed                   # returning the counted leds for each number given


n = int(input('Number of Test case:'))
digs= []
while n>0:
	dig = input('Digit:')
	digs.append(dig)
	n-=1

get = mymethod(digs)
for i in range(len(get)):
	print(get[i],'leds')

	
