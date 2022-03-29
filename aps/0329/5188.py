def f(i, j, N, s):
    global ans
    if i == N-1 and j == N-1 and s <= ans:
        ans = s
        return
    if s >= ans:
        return
    else:
        for di, dj in [[0, 1], [1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                f(ni, nj, N, s + arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 999999

    f(0, 0, N, arr[0][0])   # 처음 값 넣고 시작
    print(f'#{tc} {ans}')