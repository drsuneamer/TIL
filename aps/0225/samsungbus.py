T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노선의 개수
    L = [0] * 5001

    for i in range(1, N+1):
        # i번째 노선은 Ai ~ Bi 정류장 지남
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi+1):
            L[j] += 1

    P = int(input())
    stop = [0] * (P+1)
    for i in range(1, P+1):
        stop[i] = i

    print(f'#{tc}', end=' ')
    for i in range(1, P+1):
        print(L[stop[i]], end=" ")

