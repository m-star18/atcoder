import sys
input = sys.stdin.readline

abc = list(map(int, input().split()))
abc.sort()
if abc[0]+abc[1] == abc[2]:
    ans = "Yes"
else:
    ans = "No"
print(ans)
