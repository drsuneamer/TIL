T = int(input())
for tc in range(1, T+1):
    # 배열: N*N / M초까지 토글된다.
    N, M = map(int, input().split())
    # 문제 조건 : 행과 열 번호는 1부터 시작
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    for k in range(1, M+1): # 1초에서 M초까지
        if M % k == 0:  # M이 k의 배수이거나 K와 같은 경우 : 전체 토글
            for i in range(1, N+1):
                for j in range(1, N+1):
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    elif arr[i][j] == 0:
                        arr[i][j] = 1
        else:
            for i in range(1, N+1):
                for j in range(1, N+1):
                    if (i + j) == k or (i + j) % k == 0:
                        if arr[i][j] == 1:
                            arr[i][j] = 0
                        elif arr[i][j] == 0:
                            arr[i][j] = 1

    # 전체 영역에서 1의 개수 출력
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                ans += 1

    print(f'#{tc} {ans}')