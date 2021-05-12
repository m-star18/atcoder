s = input()
len_s = len(s)
ans = 0
for i in range(len_s):
    if s[i] == 'U':
        ans += (len_s - i - 1) + i * 2
    else:
        ans += i + (len_s - i - 1) * 2
print(ans)
