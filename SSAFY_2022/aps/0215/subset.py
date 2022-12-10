# 부분집합의 합 2022-02-15

T= int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = 12
    counts = [0] * (1 << n)
    sums = [0] * (1 << n)

    # 부분집합 원소의 개수는 counts에, 원소의 합은 sums에 저장
    for i in range(1 << n):
        cnt_n = 0
        sum_k = 0
        for j in range(n):
            if i & (1 << j):
                cnt_n += 1
                sum_k += A[j]
        counts[i] = cnt_n
        sums[i] = sum_k

    # counts의 값이 N이고, nums의 값이 K와 같은 것의 개수 세기
    result = 0
    for i in range(1 << n):
        if counts[i] == N and sums[i] == K:
            result += 1

    print(f'#{tc} {result}')