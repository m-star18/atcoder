s = input()
ans_set = [0] * len(s)

for i in range(len(s)):
    x = abs(int(s[i:i+3])-753)
    ans_set[i] = x
ans = min(ans_set)
print(ans)
