import sys
input = sys.stdin.readline


def binary_search(xy_n, n, item_x, item_y, xy_n_x, xy_n_y):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        guess = xy_n[mid][0]
        if xy_n_x - guess == item_x:
            if item_y == xy_n_y - xy_n[mid][1]:
                return False
        if xy_n_x - guess == item_x and  xy_n_y - xy_n[mid][1] < item_y:
            high = mid - 1
        elif xy_n_x - guess < item_x:
            high = mid - 1
        else:
            low = mid + 1
    # 見つからなかったとき
    return True


m = int(input())
xy_m = []
cnt = 0
x_m, y_m = map(int, input().split())

for i in range(m - 1):
    x, y = map(int, input().split())
    x = x_m - x
    y = y_m - y

    xy_m.append([x, y])

n = int(input())
xy_n = []

for i in range(n):
    x, y = map(int, input().split())
    xy_n.append([x, y])
xy_n.sort()
xy_n_x, xy_n_y = 0, 0

for i in range(n):
    xy_n_x = xy_n[i][0]
    xy_n_y = xy_n[i][1]
    for j in range(m - 1):
        item_x = xy_m[j][0]
        item_y = xy_m[j][1]

        if binary_search(xy_n, n, item_x, item_y, xy_n_x, xy_n_y):
            break

        if j == m - 2:
            print('{0} {1}'.format(xy_n_x - x_m, xy_n_y - y_m))
            exit()
