def check(x, y):
    if x == 'West':
        y = -y
    return y


n, a, b = map(int, input().split())
ans = 0

for i in range(n):
    s, d = input().split()
    d = int(d)

    if d < a:
        ans += check(s, a)
    elif a <= d <= b:
        ans += check(s, d)
    else:
        ans += check(s, b)

if ans > 0:
    print('East {0}'.format(ans))
elif ans == 0:
    print(ans)
else:
    print('West {0}'.format(abs(ans)))
