n = int(input())
s = []
for i in range(n):
    s.append(input())
    s[i] = s[i][::-1]
s.sort()
for i in range(n):
    s[i] = s[i][::-1]
    print(s[i])
