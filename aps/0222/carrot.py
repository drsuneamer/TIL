# 8702. 당근 수확  2022-02-22

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    carrots = list(map(int, input().split()))
    result = [0] * N
    w1 = w2 = 0

    for i in range(N):  # 일꾼 1이 일할 범위
        for n in range(i+1):
            w1 += carrots[n]
        for j in range(i+1, N): # 일꾼 2가 일할 범위
            w2 += carrots[j]
        if w1 > w2:
            result[i] = w1-w2
        else:
            result[i] = w2-w1
        w1 = w2 = 0

    min_index = 0
    min_result = 1e+10
    for i in range(len(result)):
        if result[i] < min_result:
            min_result = result[i]
            min_index = i+1

    print(f'#{tc} {min_index} {min_result}')
