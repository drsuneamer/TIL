T = int(input())
for tc in range(1, T+1):
    N = int(input())

    cnt = [0] * 12
    tri = 0
    run = 0

    for i in range(6):
        cnt[N % 10] += 1
        N //= 10

    for i in range(11):
        if cnt[i] >= 3:
            cnt[i] -= 3
            tri += 1
            continue

        if cnt[i] >=1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            tri += 1
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            continue
        i += 1

    if tri + run == 2:
        print('baby_gin')