a, b, c, d = map(int, input().split())

if (abs(a-b) <= d and abs(b-c) <= d) or abs(a-c) <= d:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
