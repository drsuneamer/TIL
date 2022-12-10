T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:    # 0이면 cnt는 리셋
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:    # 마지막 연속이 K인 경우
            result += 1

    # 세로
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    print(f'#{tc} {result}')
