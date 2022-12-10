T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    s = 0
    for i in range(N):
        for j in range(N):
            # 오른쪽 -> 아래 -> 왼쪽 -> 위
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N:
                    s += abs(arr[ni][nj] - arr[i][j])

    print(f'#{tc} {s}')