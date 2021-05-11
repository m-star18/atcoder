from collections import Counter

n = int(input())
s = list(input().split())
count_s = Counter(s)
if len(count_s) == 3:
    print("Three")
else:
    print("Four")
