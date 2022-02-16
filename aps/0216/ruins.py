T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    site = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    # 가로
    cnt = 0
    for i in range(N):
        for j in range(M):
            if site[i][j] == 1:
                cnt += 1
                if cnt > max_v:
                    max_v = cnt
            else:
                cnt = 0

    # 세로
    cnt = 0
    for j in range(M):
        for i in range(N):
            if site[i][j] == 1:
                cnt += 1
                if cnt > max_v:
                    max_v = cnt
            else:
                cnt = 0

    print(f'#{tc} {max_v}')