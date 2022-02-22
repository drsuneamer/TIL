T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    new90 = [[0] * N for _ in range(N)]
    new180 = [[0] * N for _ in range(N)]
    new270 = [[0] * N for _ in range(N)]

    # 90도
    for i in range(N):
        for j in range(N):
            new90[j][N-i-1] = arr[i][j]
    # 180도
    for i in range(N):
        for j in range(N):
            new180[N-i-1][N-j-1] = arr[i][j]
    # 270도
    for i in range(N):
        for j in range(N):
            new270[N-j-1][i] = arr[i][j]

    # 출력 형식에 맞게 출력
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(new90[i][j], end="")
        print(end=" ")
        for j in range(N):
            print(new180[i][j], end="")
        print(end=" ")
        for j in range(N):
            print(new270[i][j], end="")
        print()