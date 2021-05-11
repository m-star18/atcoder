import sys
input = sys.stdin.readline

x = int(input())
ans_box = [0]*8
for i in range(2, 9):
    for j in range(1, 33):
        if j**i > x:
            ans_box[i-2] = (j-1)**i
            break
print(max(ans_box))
