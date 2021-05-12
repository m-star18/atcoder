import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a, b = map(int, readline().split())
if a == b:
    print('Aoki' if n % (a + 1) == 0 and n > a else 'Takahashi')
else:
    print('Takahashi' if n <= a or a > b else 'Aoki')
