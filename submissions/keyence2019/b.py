s = input()
ans = 'keyence'
cnt = 0

for i in range(7):
    if s[i] != ans[i]:
        break
    cnt += 1

for i in range(7):
    if s[len(s) - i - 1] != ans[6 - i]:
        break
    cnt += 1

if cnt >= 7:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
