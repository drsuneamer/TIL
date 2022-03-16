def traverse(v):
    global ans
    if v:
        ans += 1
        traverse(ch1[v])
        traverse(ch2[v])

T = int(input())
for tc in range(1, T+1):
    # E: 정점 수
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    ans = 0

    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    traverse(N)
    print(f'#{tc} {ans}')
