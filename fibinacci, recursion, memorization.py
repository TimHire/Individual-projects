def fibonacci(n):
    last1, last2 = 1, 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n - 2):
            next = last1 + last2
            last1 = last2
            last2 = next
        return next

#print(fibonacci(10000))

for n in [i + 1 for i in range(1000)]:
    print(fibonacci(n))