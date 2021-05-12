import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
check = [str(i) for i in range(10)]
if all(ss in check for ss in s) and len(s) == 3:
    print(200 * int(s[0]) + 20 * int(s[1]) + int(s[2]) * 2)
else:
    print('error')
