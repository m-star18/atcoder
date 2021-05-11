import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
k = int(read())
for ss in s:
    ss = int(ss)
    if ss > 1:
        print(ss)
        break
    else:
        if k > 1:
            k -= 1
        else:
            print(ss)
            break
