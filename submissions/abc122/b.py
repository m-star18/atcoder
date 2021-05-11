s = input()
ans = [0] * 10 ** 3
cnt = 0

for i in range(len(s)):
    for j in range(1, len(s) + 1):
        memo = s[i:j]
        for k in range(len(memo)):
            if memo[k] == 'A' or memo[k] == 'C' or memo[k] == 'T' or memo[k] == 'G':
                cnt += 1
            else:
                break

        ans.append(cnt)
        cnt = 0

print(max(ans))
