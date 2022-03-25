def dfs(i, j):
    if maze[i][j] == 3:
        return 1

    else:
        maze[i][j] = 1
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                if dfs(ni, nj):
                    return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작 위치 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j


    print(f'#{tc} {dfs(sti, stj)}')