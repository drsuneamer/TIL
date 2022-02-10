T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    now_on = 0
    cnt = 0

    while now_on + K < N:
        for i in range(K, 0, -1):
            if now_on + i in stops:
                now_on += i
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')

