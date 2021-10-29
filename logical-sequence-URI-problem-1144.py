def mymethod(case):
	i = 1
	x=[]
	y=[]
	z=[]
	while i <= case:
		x.append(i)
		y.append(i*i)
		z.append(i*i*i)
		x.append(i)
		y.append(i*i+1)
		z.append(i*i*i+1)
		i = i+1
	return x,y,z

i = 0
case = int(input())
a,b,c = mymethod(case)

while i < case*2:
	print(a[i],b[i],c[i])
	i = i+1