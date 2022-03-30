T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[1])
    print(arr)
    ans = 1
    i = j = 1

    while i < N:
        if arr[i][0] >= arr[i-j][1]:
            ans += 1
            i += 1
            j = 1
        else:
            i += 1
            j += 1
    print(f'#{tc} {ans}')