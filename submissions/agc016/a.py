import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from copy import deepcopy


def moji_list(a, b):
    # アルファベット小文字 → (97, 123)
    # アルファベット大文字 → (65, 91)
    # 半角数字 → (48, 58)
    # ひらがな → (12353, 12436)
    # カタカナ → (12449, 12532+1)
    # 全角数字 → (65296, 65306)
    return [chr(i) for i in range(a, b)]


s = list(read().rstrip().decode())
ans = float('inf')
for al in moji_list(97, 123):
    cnt = 0
    check_s = deepcopy(s)
    while len(set(check_s)) > 1:
        cnt += 1
        ss = []
        for bf, af in zip(check_s, check_s[1:]):
            ss.append(af if af == al else bf)
        check_s = ss
    ans = min(ans, cnt)
print(ans)
