a = 2
b = 3
n = 2

for b in range(3,20):
	while(1):
		if n%a==0 and n%b==0:
			a = n
			print(a,b)
			break
		n += 1
	b += 1

print(n)