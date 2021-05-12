s = input()
memo = ''
len_s = len(s)
cnt = 0
ans = 0

for i in range(2 * 10 ** 5):
    ans += 1
    if memo == s[cnt]:
        if cnt == len_s - 1:
            ans -= 1
        memo = s[cnt:cnt + 2]
        cnt += 2
    else:
        memo = s[cnt]
        cnt += 1
    if cnt > len_s - 1:
        break

print(ans)
