# sys.stdin.readline()
import sys
input = sys.stdin.readline

n = int(input())
S = [list(input().split()) for i in range(n)]
for i in range(n):
    S[i].append(i)
    S[i][1]= int(S[i][1])
S = sorted(S,key=lambda x:x[1],reverse=1)
S = sorted(S,key=lambda x:x[0])
for i in range(n):
    print(S[i][2]+1)
