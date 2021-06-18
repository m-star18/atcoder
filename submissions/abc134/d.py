import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


n = int(readline())
a = list(map(int, readline().split()))
a = a[::-1]
cnt = [0] * n
ans = []
for i in range(n):
    if cnt[n - i - 1] % 2 != a[i]:
        ans.append(n - i)
        memo = make_divisors(n - i)
        for j in range(len(memo)):
            cnt[memo[j] - 1] += 1
print(len(ans))
print(*ans[::-1])
