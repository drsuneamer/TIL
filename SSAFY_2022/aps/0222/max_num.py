T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    max_v = L[0]

    for n in L:
        if n > max_v:
            max_v = n

    print(f'#{tc} {max_v}')