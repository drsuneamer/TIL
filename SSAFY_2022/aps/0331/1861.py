def bfs(i, j):
    global start, ans
    q = []
    s = []

    v[i][j] = 1
    q.append([i, j])
    s.append(rooms[i][j])

    while q:
        si, sj = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and abs(rooms[ni][nj] - rooms[si][sj]) == 1:
                q.append([ni, nj])
                s.append(rooms[ni][nj])
                v[ni][nj] = 1


    if len(s) > ans:
        ans = len(s)
        start = min(s)
    if len(s) == ans and min(s) < start:
        ans = len(s)
        start = min(s)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    start = 0
    ans = 0

    # 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는가?
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                bfs(i, j)

    print(f'#{tc} {start} {ans}')
