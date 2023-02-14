m = int(input())
n = int(input())
n_list = []
for i in range(m, n+1):
    if i == 1:
        continue
    elif i == 2:
        n_list.append(i)
    else:
        check = 0
        for j in range(2, i):
            if (i % j) == 0:
                check = 1
                break
        if check == 0:
            n_list.append(i)
if len(n_list) == 0:
    print(-1)
else:
    print(sum(n_list))
    print(min(n_list)) 