T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 조건을 만족하는 예비 후보지의 개수 (사진 가능 방향 4개 이상)
    ans = 0

    for i in range(N):
        for j in range(M):
            cnt = 0
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    if 0 <= ii < N and 0 <= jj < M:
                        if arr[ii][jj] < arr[i][j]:
                            cnt += 1
            if cnt >= 4:
                ans += 1

    print(f'#{tc} {ans}')
