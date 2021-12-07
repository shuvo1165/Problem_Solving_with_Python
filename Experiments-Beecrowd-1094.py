n = int(input())
total=0 
Couelho=0
Rato=0
Sapo = 0
for i in range(n):
	number, category = map(str,input().split())
	if number.isdigit() and 1<= int(number) <=15:
		number = int(number)
		total+=number
		if category=='C':
			Couelho+=number
		elif category=='R':
			Rato+=number
		elif category=='S':
			Sapo+=number
		else:
			break
		
	else:
		break
print('Total: %d cobaias'%total)
print('Total de coelhos: %d'%Couelho)
print('Total de ratos: %d'%Rato)
print('Total de sapos: %d'%Sapo)
print('Percentual de coelhos: {:0.2f} %'.format(Couelho/total*100))
print('Percentual de ratos: {:0.2f} %'.format(Rato/total*100))
print('Percentual de sapos: {:0.2f} %'.format(Sapo/total*100))

