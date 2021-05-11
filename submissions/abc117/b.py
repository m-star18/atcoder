n = int(input())
l = [int(_) for _ in input().split()]

maxs = max(l)
if maxs < sum(l)-maxs:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
