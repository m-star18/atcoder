import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
match = [a, b, c]
cnt = 0

for i in range(3):
    if match[i] == 5:
        cnt += 2
    elif match[i] == 7:
        cnt += 1

if cnt == 5:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)
