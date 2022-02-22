T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [[] for _ in range(N)]

    # 1로만 구성된 첫 행과 두 번째 행 설정
    result[0] = [1]
    if N > 1:
        result[1] = [1, 1]

    for i in range(2, N):
        result[i].append(1)     # 맨 앞의 1 삽입
        for j in range(1, i):
            result[i].append(result[i-1][j-1] + result[i-1][j])     # 왼쪽과 오른쪽 위의 숫자의 합
        result[i].append(1)     # 맨 뒤의 1 삽입

    print(f'#{tc}')
    for i in range(N):
        print(*result[i])