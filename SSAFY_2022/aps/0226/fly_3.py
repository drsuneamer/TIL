T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # +
    di1 = [0, 1, 0, -1]
    dj1 = [1, 0, -1, 0]

    # x (오른쪽 위부터)
    di2 = [-1, 1, 1, -1]
    dj2 = [1, 1, -1, -1]

    for i in range(N):
        for j in range(N):
            # 중앙 값은 미리 한번만 더해줌
            fly1 = arr[i][j]    # +
            fly2 = arr[i][j]    # *
            for k in range(4):
                for m in range(1, M):
                    i1 = i + (di1[k] * m)   # +
                    j1 = j + (dj1[k] * m)
                    if 0 <= i1 < N and 0 <= j1 < N:
                        fly1 += arr[i1][j1]

                    i2 = i + (di2[k] * m)   # x
                    j2 = j + (dj2[k] * m)
                    if 0 <= i2 < N and 0 <= j2 < N:
                        fly2 += arr[i2][j2]
            if fly1 > ans:
                ans = fly1
            if fly2 > ans:
                ans = fly2

    print(f'#{tc} {ans}')