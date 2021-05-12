import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
w = [readline().rstrip().decode() for i in range(n)]
check = [w.pop(0)]
for ww in w:
    if check[-1][-1] == ww[0] and ww not in check:
        check.append(ww)
    else:
        if len(check) % 2 == 0:
            print('LOSE')
        else:
            print('WIN')
        exit()
print('DRAW')
