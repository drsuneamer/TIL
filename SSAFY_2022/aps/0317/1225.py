for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    n = 1
    cnt = 0

    while 1:
        cnt += 1
        if i > 7:
            i = 0
        if n > 5:
            n = 1
        if arr[i] - n <= 0:
            arr[i] = 0
            break
        arr[i] -= n
        i += 1
        n += 1

    print(f'#{tc}', end=" ")
    cnt = cnt % 8
    for i in range(cnt, 8):
        print(arr[i], end=" ")
    for i in range(0, cnt):
        print(arr[i], end=" ")
    print()



