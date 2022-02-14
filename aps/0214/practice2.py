T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)

    for i in range(1, 1 << n):
        s = 0
        for j in range(n):
            if i & (1 << j):
                s += arr[j]
        if s == 0:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')