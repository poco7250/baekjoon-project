def d(n : int) -> int:
    result = n + (n // 1000) + ((n % 1000) // 100) + (((n % 1000) % 100) // 10) + (n % 10)
    return result

n_list = [i for i in range(10000)]
for i in range(10000):
    if d(i) in n_list:
        n_list.remove(d(i))
for i in range(len(n_list)):
    print(n_list[i])