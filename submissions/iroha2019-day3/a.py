import sys
input = sys.stdin.readline

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = map(int, input().split())
print(a - b)
print(c + d)
print(max(0, f - e + 1))
print((g + h + i) // 3 + 1)
print(['', 'a', 'aa', 'aaa', 'aaai', 'aaaji', 'aabaji', 'agabaji', 'dagabaji'][j])

kk = k
while kk % 61 != l:
    kk += 59
kk += 59 * 61 * (m - 1)

prf = iter([6, 28, 496, 8128, 33550336, 8589869056])
nn = next(prf)
while abs(kk - nn) < n:
    nn = next(prf)

print(min(kk, nn))
print(max(kk, nn))
print((o + p + q) * (r + s + t) * (u + v + w) * (x + y + z) % 9973)
