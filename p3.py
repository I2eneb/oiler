a = 600851475143
n = 3

while(1):
	if n>=a:
		break
	while(1):
		if a%n == 0:
			a /= n
			print(n)
			n = 3
			break
		n += 1