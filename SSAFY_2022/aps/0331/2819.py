def bfs(i, j, s):
    q = []
    q.append([i, j])

    while q:
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 4 and 0 <= nj < 4 and



T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    visited = [[0] * 4 for _ in range(4)]

    bfs(0, 0, '')


