import sys
import collections
input = sys.stdin.readline

s = input()
S = collections.Counter(s)
if s.count(S.most_common()[0][0]) == 2 and s.count(S.most_common()[1][0]) == 2:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
