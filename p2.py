a, b, c = 1, 2, 3
s = 2 #sum

while(1) :
	a = b+c
	b = c
	c = a
	if (a%2==0):
		s += a
	if (a > 4000000):
		break
print(s)