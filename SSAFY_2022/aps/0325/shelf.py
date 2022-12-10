def f(i, N, B):
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += lst[j]
        if s >= B:
            result.append(s)
    else:
        bit[i] = 1
        f(i+1, N, B)
        bit[i] = 0
        f(i+1, N, B)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    bit = [0] * N
    result = []

    f(0, N, B)
    print(f'#{tc} {min(result) - B}')