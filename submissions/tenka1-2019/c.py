N = int(input())
S = input()
a = S.count('.')
ans = a

for i in S:
    if i == '.':
        a -= 1
    else:
        a += 1
    ans = min(ans, a)

print(ans)
