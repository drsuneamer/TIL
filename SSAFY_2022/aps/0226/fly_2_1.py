T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly = 0
            for k in range(M):
                fly += arr[i+k][j+k]        # 왼쪽 위부터 대각선
                fly += arr[i+k][j+M-1-k]    # 오른쪽 위부터 대각선
            if M % 2:
                fly -= arr[i + M // 2][j + M // 2]  # M이 홀수이면 가운데 값이 두 번 더해짐
            if fly > ans:
                ans = fly

    print(f'#{tc} {ans}')