def n_seq(n : int) -> int:
    count = 0
    for i in range(1, n+1):
        if i >= 100:
            f = i // 100
            s = (i % 100) // 10
            t = i % 10
            if (f-s) == (s-t):
                count += 1
        else:
            count += 1
    return count

n = int(input())
print(n_seq(n))
