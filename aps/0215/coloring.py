T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 100 for _ in range(100)]
    for i in range(N):
        i1, j1, i2, j2, color = map(int, input().split())

        if color == 1:      # 빨간색에 해당하는 값에 1 더하기
            for r in range(i1, i2+1):
                for c in range(j1, j2+1):
                    arr[r][c] += 1

        else:           # 파란색에 2 더하기
            for r in range(i1, i2 + 1):
                for c in range(j1, j2 + 1):
                    arr[r][c] += 2

    cnt = 0     # 보라색(3)인 값 찾아 숫자 세기
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')