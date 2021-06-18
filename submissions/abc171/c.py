def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    def moji_list(a, b):
        # アルファベット小文字 → (97, 123)
        # アルファベット大文字 → (65, 91)
        # 半角数字 → (48, 58)
        # ひらがな → (12353, 12436)
        # カタカナ → (12449, 12532+1)
        # 全角数字 → (65296, 65306)
        return [chr(i) for i in range(a, b)]


    n = int(readline())
    al = ['z'] + moji_list(97, 123)
    ans = ''
    for i in range(1, 10 ** 6):
        n, check = divmod(n, 26)
        if check == 0:
            n -= 1
        ans += al[check]
        if n == 0:
            print(ans[::-1])
            break


if __name__ == '__main__':
    main()
