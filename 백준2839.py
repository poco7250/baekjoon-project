n = int(input())
result = -1
count = 0
if (n % 5) == 0:
    result = (n // 5)
    print(result)
else:
    p = 0
    while n > 0:
        n -= 3
        p += 1
        if n % 5 == 0:
            p += n // 5
            print(p)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(p)
            break 