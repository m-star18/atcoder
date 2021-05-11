n = int(input())
s = input()
memo = [0] * (n + 1)
cnt = 0
for i in range(n):
    if s[i] == 'I':
        cnt += 1
    else:
        cnt -= 1
    memo[i] = cnt
print(max(memo))
