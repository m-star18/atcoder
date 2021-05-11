import collections

n = int(input())
s = []
for i in range(n):
    s.append(input())
Count_s = collections.Counter(s)
ans = Count_s.most_common()[0][0]
print(ans)
