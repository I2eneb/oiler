a, b, result = 0, 0, 0
for i in range(1, 100):
    for j in range(1, 100):
        result = (1000-i) * (1000-j)
        a = list(str(result))
        b = a
        if a == b[::-1]:
            print(result)
            break