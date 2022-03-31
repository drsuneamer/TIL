def f(i, N):
    if i == N:
        cnt(p)

    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[j], p[i] = p[i], p[j]


def cnt(lst):
    global ans
    v = 0
    for i in range(N):
        if arr[i][lst[i]] != 0:
            v += arr[i][lst[i]]
        else:
            v = 0
            return
    print(v)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [x for x in range(N)]
    ans = N * 100

    f(0, N)
    print(ans)