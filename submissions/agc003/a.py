import sys
input = sys.stdin.readline

s = input()
cnt = 0
if 'N' in s and 'S' in s:
    cnt += 1
elif 'N' not in s and 'S' not in s:
    cnt += 1
if 'W' in s and 'E' in s:
    cnt += 1
elif 'W' not in s and 'E' not in s:
    cnt += 1
if cnt == 2:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
