s = input()
k = int(input())
mod = k % len(s)

for i in range(len(s)):
    if i == 0:
        ans = s[mod]
    elif mod+i >= len(s):
        ans += s[mod+i-len(s)]
    else:
        ans += s[mod+i]
print(ans)
