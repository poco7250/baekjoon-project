m, n = map(int, input().split())
for i in range(m, n+1):
    if i == 1:
        continue
    elif i == 2:
        print(i)
    else:
        check = 0
        for j in range(2, i):
            if (i % j) == 0:
                check = 1
                break
        if check == 0:
            print(i) 