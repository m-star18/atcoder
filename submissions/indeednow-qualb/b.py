s = input()
t = input()
ans = -1
for i in range(len(s)):
    tmp_s = s[len(s)-i:] + s[:len(s)-i]
    if t == tmp_s:
        ans = i
        break
print(ans)
