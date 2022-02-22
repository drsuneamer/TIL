T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 회전 방향 : 오른쪽 - 아래 - 왼쪽 - 위
    di = (0, 1, 0, -1)  # 행
    dj = (1, 0, -1, 0)  # 열

    d = 1   # 입력 숫자
    i = 0   # 시작 행
    j = 0   # 시작 열
    k = 0   # 진행 방향 (시작-오른쪽)

    while d <= N * N:   # 마지막 숫자 (N^2까지)
        if 0 <= i < N and 0 <= j < N and arr[i][j] == 0:
            arr[i][j] = d
            i, j = i + di[k], j + dj[k]
            d += 1
        else:
            i -= di[k]
            j -= dj[k]
            k = (k+1) % 4
            i, j = i + di[k], j + dj[k]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
