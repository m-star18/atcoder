import sys
input = sys.stdin.readline

n = int(input())
c = input()
ans = [c.count('1'), c.count('2'), c.count('3'), c.count('4')]
print(max(ans), min(ans))
