s = input()
cnt = 0
ans = s[0]
for i in range(1, len(s)):
    if s[i] == ans[-1]:
        if s[i] == '0':
            ans += '1'
        else:
            ans = '0'
        cnt += 1
    else:
        ans += s[i]
print(cnt)
