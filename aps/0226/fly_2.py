T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly = 0
            for ii in range(i, i + M):
                if ii == i or ii == i + M - 1:  # 첫 행과 마지막 행
                    fly += arr[ii][j]
                    fly += arr[ii][j + M - 1]
                else:
                    for jj in range(j + 1, j + M - 1):
                        fly += arr[ii][jj]
            if fly > ans:
                ans = fly

    print(f'#{tc} {ans}')