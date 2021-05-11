#入力
H,W=map(int,input().split())
h,w=map(int,input().split())
#計算
B_cells=h*W+w*H-h*w #黒色のマス目の数
W_cells=H*W-B_cells #白色のマス目の数
#出力
print(W_cells)
