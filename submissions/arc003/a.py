import sys
input = sys.stdin.readline

n = int(input())
r = input()
A = r.count('A')
B = r.count('B')
C = r.count('C')
D = r.count('D')
ans = (A*4+B*3+C*2+D*1) / n
print(ans)
