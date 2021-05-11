import sys
input = sys.stdin.readline

n = input().rstrip('\n')
cnt = 0
for i in range(len(n)):
    cnt += int(n[i])

if int(n) % cnt == 0:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
