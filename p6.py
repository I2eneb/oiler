sum_a = 0
sum_b = 0

for i in range(1,100+1):
	sum_a += i*i
for i in range(1,100+1):
	sum_b += i

print((sum_b*sum_b)-sum_a)