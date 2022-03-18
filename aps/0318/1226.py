def bfs(i, j):
    visited = [[0] * 16 for _ in range(16)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))  # 인큐
                visited[ni][nj] = visited[i][j] + 1
    return 0



for tc in range(1, 11):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                si, sj = i, j

    print(f'#{tc} {bfs(si, sj)}')
