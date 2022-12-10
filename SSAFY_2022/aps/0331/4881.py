def perm(i, N, s):
    global ans
    if i == N:
        if ans > s:
            ans = s
    elif s > ans:
        return
    else:
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            perm(i + 1, N, s + arr[i][A[i]])
            A[j], A[i] = A[i], A[j]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 100000

    A = [x for x in range(N)]
    perm(0, N, 0)

    print(f'#{tc} {ans}')