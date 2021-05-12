import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

b = list(map(str, readline().rstrip().decode()))
n = int(readline())
a = sorted([int(readline()) for i in range(n)])
a = list(map(str, a))
for i in range(n):
    for j in range(n - 1):
        if len(a[j]) < len(a[j + 1]):
            continue
        else:
            for check_1, check_2 in zip(a[j], a[j + 1]):
                flag = False
                for bb in b:
                    if bb != check_1 and bb == check_2:
                        flag = True
                        a[j], a[j + 1] = a[j + 1], a[j]
                        break
                    if bb == check_1 and bb != check_2:
                        flag = True
                        break
                if flag:
                    break
print('\n'.join(a))
