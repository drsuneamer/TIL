T = int(input())
for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 1

    # 가로
    for i in range(9):
        for j in range(9):
            s = arr[i][j]
            for k in range(1, 9-j):
                if s == arr[i][j+k]:
                    result = 0
                    break

    # 세로
    if result == 0:
        for j in range(9):
            for i in range(9):
                s = arr[i][j]
                for k in range(1, 9 - i):
                    if s == arr[i+k][j]:
                        result = 0
                        break

    # 사각형
    square = [[0] * 9 for _ in range(9)]
    a = [0, 1, 2]
    b = [3, 4, 5]
    c = [6, 7, 8]

    cnt = 0
    for i in range(3):
        for j in range(3):
            arr[i][j] = square[0][cnt]
            cnt += 1
