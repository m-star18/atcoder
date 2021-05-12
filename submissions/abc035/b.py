s = input()
t = int(input())
xy = [0, 0]
cnt = 0
for i in range(len(s)):
  if s[i] == 'U':
    xy[1] += 1
  elif s[i] == 'D':
    xy[1] -= 1
  elif s[i] == 'R':
    xy[0] += 1
  elif s[i] == 'L':
    xy[0] -= 1
  else:
    cnt += 1
ans = abs(xy[0]) + abs(xy[1])
if t == 1:
  ans += cnt
else:
  if ans >= cnt:
    ans -= cnt
  else:
    ans = (ans - cnt) % 2
print(ans)
