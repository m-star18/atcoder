import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
bf = int(readline())
for i in range(n - 1):
    af = int(readline())
    if bf > af:
        print('down ' + str(bf - af))
    elif bf == af:
        print('stay')
    else:
        print('up ' + str(af - bf))
    bf = af
