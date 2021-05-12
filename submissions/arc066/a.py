import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n = int(readline())
a = list(map(int, readline().split()))
counter = sorted(list(Counter(a).items()))
if n % 2 == 1:
    if counter[0] != (0, 1):
        print(0)
        exit()
    else:
        memo = 2
        counter.pop(0)
else:
    memo = 1
for k, v in counter:
    if memo != k or v != 2:
        print(0)
        exit()
    memo += 2
mod = 10 ** 9 + 7
print(pow(2, len(counter), mod))
