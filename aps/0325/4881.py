def min_sum(i):
    global ans
    visited = [0] * N
    lst = [0] * N
    if i == N:
        if sum(lst) < ans:
            ans = sum(lst)

    # 행 번호: 0, 1, 2 순서대로 고정정
   for i in range(N):
        for j in range(N):
            s == arr[si][sj]




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
