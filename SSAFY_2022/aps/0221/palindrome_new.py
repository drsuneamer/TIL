T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    result = 1

    for M in range(100, 1, -1):     # 가로
        for i in range(100):
            for n in range(100 - M + 1):
                cnt = 0
                for j in range(M//2):
                    if arr[i][n + j] == arr[i][n + M - j - 1]:
                        cnt += 1
                    else:
                        cnt += 0
                        break
                if cnt == M // 2:
                    result = M
                    break
            if result > M:
                break
        if result > M:
            break

    for M in range(100, 1, -1):     # 세로
        for j in range(100):
            for n in range(100 - M + 1):
                cnt = 0
                for i in range(M//2):
                    if arr[n + i][j] == arr[n+M-i-1][j]:
                        cnt += 1
                    else:
                        cnt += 0
                        break
                if cnt == M // 2:
                    result = M
                    break
            if result > M:
                break
        if result > M:
            break

    print(f'#{tc}', result)