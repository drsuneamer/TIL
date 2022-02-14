T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * 100 for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    # 행의 합, 열의 합
    max_row, max_col = 0, 0
    for i in range(100):
        row_sum, col_sum = 0, 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        if row_sum > max_row:
            max_row = row_sum
        if col_sum > max_col:
            max_col = col_sum

    # 대각선의 합 (1-100)
    max_d1, d1_sum, max_d2, d2_sum = 0, 0, 0, 0
    for i in range(100):
        d1_sum += arr[i][i]
        d2_sum += arr[i][99 - i]
    if d1_sum > max_d1:
        max_d1 = d1_sum
        d1_sum = 0
    else:
        d1_sum = 0

    if d2_sum > max_d2:
        max_d2 = d2_sum
        d2_sum = 0
    else:
        d2_sum = 0

    sums = [max_row, max_col, max_d1, max_d2]
    result = 0
    for i in sums:
        if i > result:
            result = i

    print(f'#{tc} {result}')