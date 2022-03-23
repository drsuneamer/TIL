T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stops = [0] * 5001

    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            stops[j] += 1

    print(f'#{tc}', end=" ")
    P = int(input())
    for i in range(P-1):
        s = int(input())
        print(stops[s], end=" ")

    s = int(input())
    print(stops[s])
