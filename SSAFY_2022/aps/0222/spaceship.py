T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            num = arr[i][j]
            cnt = 0
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    if arr[ii][jj] < num:
                        cnt += 1
            if cnt >= 4:
                result += 1

    print(f'#{tc} {result}')