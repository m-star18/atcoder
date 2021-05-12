import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, a, b, c = map(int, readline().split())
s = [readline().rstrip().decode() for _ in range(n)] + ['']
ans = [''] * n
for i, (bf, af) in enumerate(zip(s, s[1:])):
    if bf == 'AB':
        if a > b or (a == b and i != n - 1 and 'B' in af):
            b += 1
            a -= 1
            ans[i] = 'B'
        else:
            a += 1
            b -= 1
            ans[i] = 'A'
    elif bf == 'AC':
        if a > c or (a == c and i != n - 1 and 'C' in af):
            c += 1
            a -= 1
            ans[i] = 'C'
        else:
            c -= 1
            a += 1
            ans[i] = 'A'
    else:
        if b > c or (b == c and i != n - 1 and 'C' in af):
            c += 1
            b -= 1
            ans[i] = 'C'
        else:
            c -= 1
            b += 1
            ans[i] = 'B'
    if a < 0 or b < 0 or c < 0:
        print('No')
        exit()
print('Yes')
print('\n'.join(ans))
