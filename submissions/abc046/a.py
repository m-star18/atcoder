import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
abc = [a, b, c]
abc = list(set(abc))
print(len(abc))
