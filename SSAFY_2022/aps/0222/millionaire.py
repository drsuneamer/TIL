T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    max_v = arr[N-1]

    for i in range(N-2, -1, -1):
        if arr[i] < max_v:
            result += max_v - arr[i]
        else:
            max_v = arr[i]

    print(f'#{tc} {result}')