def enq(v):
    global last
    if v <= N:
        last += 1
        tree[last] = arr[v]
        c = last
        p = c // 2
        while p >= 1 and tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            c = p
            p = c // 2
        enq(v+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 0

    enq(1)

    anc = []
    while N // 2 > 0:
        anc.append(tree[N//2])
        N //= 2

    print(f'#{tc} {sum(anc)}')