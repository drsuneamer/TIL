T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = [0] * N

    for i in range(N):
        for j in range(1, N-i):
            if arr[i] > arr[i+j]:
                cnt[i] += 1

    max_v = cnt[0]
    for i in cnt:
        if i > max_v:
            max_v = i

    print(max_v)

