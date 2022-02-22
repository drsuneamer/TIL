T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 회문 범위 내의 첫 글자와 마지막 글자부터 안쪽으로 순서대로 비교
    # 가로
    for i in range(N):  # 행 번호
        for n in range(N - M + 1):  # 가로줄 판독 횟수
            cnt = 0
            for j in range(M//2):
                if arr[i][n+j] == arr[i][n+M-j-1]:
                    cnt += 1
                else:
                    cnt = 0
                    break
            if cnt == M // 2:
                print(f'#{tc}', end=" ")
                for k in range(M):
                    print(arr[i][n+k], end="")
                print()

    # 세로
    for j in range(N):  # 열 번호
        for n in range(N - M + 1):  # 세로줄 판독 횟수
            cnt = 0
            for i in range(M//2):
                if arr[n+i][j] == arr[n+M-i-1][j]:
                    cnt += 1
                else:
                    cnt = 0
                    break
            if cnt == M // 2:
                print(f'#{tc}', end=" ")
                for k in range(M):
                    print(arr[n+k][j], end="")
                print()