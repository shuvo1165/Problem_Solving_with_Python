def mymethod(n):
    
    
    
    numbers = [2]
    for i in range(1,10000):
    	result = 0
    	if i%n == 0:
		    result = i +2 
		    numbers.append(result)
    return numbers

n = int(input('Enter value:'))
x = mymethod(n)
for i in range(len(x)):
	print('%d'%x[i])