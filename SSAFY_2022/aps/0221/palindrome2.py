T = 1
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    result = 1

    # 회문의 길이 = s (100부터 거꾸로)
    # 행의 길이 : 100 / 열의 길이 : 100
    # 가장 긴 회문 찾기: 찾으면 max(result) 값과 비교 후 break

    # 길이가 100인 회문부터 찾아보자
    for M in range(100, 1, -1):
        for i in range(N):  # 행 번호
            for n in range(N - M + 1):  # 가로줄 판독 횟수
                cnt = 0
                for j in range(M // 2):
                    if arr[i][n + j] == arr[i][n + M - j - 1]:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == M // 2:
                    if M > result:
                        result = M
                        break
            if M == result:
                break
        if M == result:
            break

    for M in range(100, 1, -1):
        for j in range(N):  # 행 번호
            for n in range(N - M + 1):  # 가로줄 판독 횟수
                cnt = 0
                for i in range(M // 2):
                    if arr[n+i][j] == arr[n+M-i-1][j]:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == M // 2:
                    if M > result:
                        result = M
                        break
            if M == result:
                break
        if M == result:
            break

    print(result)