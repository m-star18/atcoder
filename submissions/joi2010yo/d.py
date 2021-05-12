import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import combinations, permutations

n = int(readline())
k = int(readline())
c = [readline().rstrip().decode() for _ in range(n)]
ans = set()
for comb in combinations(c, k):
    for num in permutations(comb):
        ans.add(''.join(num))
print(len(ans))
