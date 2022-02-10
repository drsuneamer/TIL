T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    result = [0] * (N-M+1)

    for i in range(N-M+1):
        sum_n = 0
        for j in range(M):
            sum_n += nums[i+j]
        result[i] = sum_n

    max_n = result[0]
    min_n = result[0]
    for i in result:
        if i > max_n:
            max_n = i
        if i < min_n:
            min_n = i

    print(f'#{tc} {max_n - min_n}')
