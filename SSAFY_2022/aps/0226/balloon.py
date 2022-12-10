T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]
    # 오른쪽 - 아래 - 왼쪽 - 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ans = 0

    for i in range(N):
        for j in range(M):
            num = balloons[i][j]
            total = 0
            total += num    # 현재 칸의 값도 포함
            for k in range(4):
                for n in range(1, num+1):
                    ii = i + (di[k] * n)
                    jj = j + (dj[k] * n)
                    # N과 M은 인덱스 범위 밖인 것 잊지 말기!!!
                    if 0 <= ii < N and 0 <= jj < M:
                        total += balloons[ii][jj]
            if total > ans:
                ans = total

    print(f'#{tc} {ans}')