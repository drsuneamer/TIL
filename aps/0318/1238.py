def BFS(s):
    q = []  # 사용할 큐
    v = [0] * 101   # 방문 기록

    q.append(s) # 큐에 연락 시작 값 기록
    v[s] = 1    # 시작 값 방문 기록

    while q:    # 큐에 값이 있는 동안
        a = q.pop(0)    # 가장 앞에 있는 값 pop
        # 연결 값 확인해서 q에 넣고 v에 넣기
        for j in range(1, 101):
            if adj[a][j] == 1 and v[j] == 0:
                q.append(j)
                v[j] = v[a] + 1
    return v


for tc in range(1, 11):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[0] * 101 for _ in range(101)]

    # from - to 입력
    for i in range(0, N, 2):
        adj[lst[i]][lst[i+1]] = 1

    V = BFS(S)
    max_v = 0
    ans = 0
    for i in range(1, 101):
        if V[i] >= max_v:
            max_v = V[i]
            ans = i
    print(f'#{tc} {ans}')