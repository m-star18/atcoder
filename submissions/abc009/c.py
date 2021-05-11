import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n, k = map(int, readline().split())
s = readline().rstrip().decode('utf-8')


def check(use, make, k):
    return sum((use - make).values()) <= k


def make_ans(s, use, make, k):
    if len(s) == 0:
        return ''
    for x in sorted(x for x, n in make.items() if n):
        use[s[0]] -= 1
        make[x] -= 1
        kk = k
        if s[0] != x:
            kk -= 1
        if check(use, make, kk):
            return x + make_ans(s[1:], use, make, kk)
        use[s[0]] += 1
        make[x] += 1


print(make_ans(s, Counter(s), Counter(s), k))
