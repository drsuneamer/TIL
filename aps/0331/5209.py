def cost(i, N, s):  # s = 현재까지의 생산 비용
    global ans

    if i == N:
        if s < ans:
            ans = s
    elif s > ans:   # 현재 최소값 넘어서면
        return
    else:
        for j in range(i, N):
            lst[i], lst[j] = lst[j], lst[i]
            cost(i+1, N, s+arr[i][lst[i]])     # 행 값은 1씩 증가
            lst[j], lst[i] = lst[i], lst[j]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 99 * 15
    # 열 값 저장할 배열
    lst = [x for x in range(N)]
    cost(0, N, 0)

    print(f'#{tc} {ans}')