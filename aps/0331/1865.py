def success(i, N, p):
    global ans
    if i == N:
        if p * 100 > ans:
            ans = round(p * 100, 6)
    elif p * 100 <= ans:
        return

    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            success(i+1, N, p * (W[i][P[i]]) / 100)
            P[j], P[i] = P[i], P[j]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    P = [x for x in range(N)]
    ans = 0

    success(0, N, 1)
    print(f'#{tc}', '{:.6f}'.format(ans))