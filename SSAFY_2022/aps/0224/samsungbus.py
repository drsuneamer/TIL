T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노선의 개수
    D = {}

    for i in range(1, N+1):
        # i번째 노선은 Ai ~ Bi 정류장 지남
        A, B = map(int, input().split())
        for j in range(A, B+1):
            D[j] = D.get(j, 0) + 1

    P = int(input())
    stop = []
    for i in range(1, P+1):
        stop.append(i)

    print(f'#{tc}', end=' ')
    for i in range(1, P+1):
        print(D[stop[i]], end=" ")
