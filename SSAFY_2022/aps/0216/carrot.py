T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    cnt = 1
    max_cnt = 1

    for i in range(N - 1):
        if carrots[i] < carrots[i + 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')