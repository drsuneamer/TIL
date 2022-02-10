T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2):
        around = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        minus_num = around[0]
        for j in around:
            if minus_num < j:
                minus_num = j
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            cnt += arr[i] - minus_num

    print(f'#{tc} {cnt}')