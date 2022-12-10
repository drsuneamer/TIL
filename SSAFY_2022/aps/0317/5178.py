def f(v):
    if v > 0:
        if (v*2+1) <= N:
            tree[v] = tree[v*2] + tree[v*2+1]
        else:
            tree[v] = tree[v*2]
        f(v-1)

T = int(input())
for tc in range(1, T+1):
    # N: 노드의 개수  M: 리프 노드의 개수  L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    f(N-M)
    print(f'#{tc} {tree[L]}')



