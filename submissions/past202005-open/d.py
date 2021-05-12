import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = [readline().rstrip().decode() for _ in range(5)]
m0 = ['###', '#.#', '#.#', '#.#', '###']
m1 = ['.#.', '##.', '.#.', '.#.', '###']
m2 = ['###', '..#', '###', '#..', '###']
m3 = ['###', '..#', '###', '..#', '###']
m4 = ['#.#', '#.#', '###', '..#', '..#']
m5 = ['###', '#..', '###', '..#', '###']
m6 = ['###', '#..', '###', '#.#', '###']
m7 = ['###', '..#', '..#', '..#', '..#']
m8 = ['###', '#.#', '###', '#.#', '###']
m9 = ['###', '#.#', '###', '..#', '###']
m = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9]
ans = ''
for idx in range(n):
    for i, mm in enumerate(m):
        for jdx, ss in enumerate(s):
            if ss[idx * 4 + 1:(idx + 1) * 4] != mm[jdx]:
                break
        else:
            ans += str(i)
            break
print(ans)
