import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
al = [chr(ord('a') + i) for i in range(26)] + ['.']
ans = set()
for x in al:
    for y in al:
        for z in al:
            for i in range(len(s) - 2):
                ss = s[i:i + 3]
                if (x == '.' or x == ss[0]) and (y == '.' or y == ss[1]) and (z == ss[2] or z == '.'):
                    ans.add(x + y + z)
        for i in range(len(s) - 1):
            ss = s[i:i + 2]
            if (x == '.' or x == ss[0]) and (y == '.' or y == ss[1]):
                ans.add(x + y)
    for ss in s:
        if x == ss[0] or x == '.':
            ans.add(x)
print(len(ans))
