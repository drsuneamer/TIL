T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = [[0] * (N-M+1) for _ in range(N-M+1)]   # 죽은 파리 개수 저장할 리스트

    # (0,0)부터 시작하여 칸을 넘어가지 않는 범위 안에서 파리 합 찾기
    for di in range(N-M+1):
        for dj in range(N-M+1):
            cnt = 0
            for i in range(di, di+M):
                for j in range(dj, dj+M):
                    cnt += arr[i][j]
            a[di][dj] = cnt

    # 가장 큰 수의 값
    max_n = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if a[i][j] > max_n:
                max_n = a[i][j]
    print(f'#{tc} {max_n}')