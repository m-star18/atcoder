s = input()
ans = 'CODEFESTIVAL2016'
cnt = 0
for i in range(len(s)):
  if s[i] != ans[i]:
    cnt += 1
print(cnt)
