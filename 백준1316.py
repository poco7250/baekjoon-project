n = int(input())
count = 0

for i in range(n):
    s = input()
    a_list = []
    for j in range(len(s)):
        if s[j] in a_list:
            if s[j] != s[j-1]:
                count -= 1
                break
        else:
            a_list.append(s[j])
    count += 1
print(count)