import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def Z_algo(S):
    n = len(S)
    LCP = [0] * n
    c = 0  # 最も末尾側までLCPを求めたインデックス
    for i in range(1, n):
        # i番目からのLCPが以前計算したcからのLCPに含まれている場合
        if i + LCP[i - c] < c + LCP[c]:
            LCP[i] = LCP[i - c]
        else:
            j = max(0, c + LCP[c] - i)
            while i + j < n and S[j] == S[i + j]:
                j += 1
            LCP[i] = j
            c = i
    LCP[0] = n
    return LCP


n = int(readline())
s = read().rstrip().decode()
ans = 0
for i in range(n):
    for j, m in enumerate(Z_algo(s[i:])):
        ans = max(ans, min(j, m))
print(ans)
