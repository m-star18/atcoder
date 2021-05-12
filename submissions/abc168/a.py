import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = read().rstrip().decode()[::-1]
hon = ['2', '4', '5', '7', '9']
pon = ['0', '1', '6', '8']
if n[0] in hon:
    print('hon')
elif n[0] in pon:
    print('pon')
else:
    print('bon')
