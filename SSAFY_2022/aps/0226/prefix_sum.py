T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 모든 행의 구간합 중 최대값
    ans = 0

    for i in range(N):
        p_sum = 0
        for j in range(i, i + K):
            if j < N:
                p_sum += arr[i][j]
        if p_sum > ans:
            ans = p_sum

    print(f'#{tc} {ans}')

