T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input()))
    cnt = [0] * 12
    for i in range(6):
        cnt[card[i]] += 1

    r = 0
    t = 0
    i = 0

    while i < 10:
        if cnt[i] >= 3:
            cnt[i] -= 3
            t += 1
            continue
        if cnt[i]>0 and cnt[i+1]>0 and cnt[i+2]>0:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            r += 1
            continue
        i += 1
    if t + r == 2:
        print(f'{tc} Baby Gin')
    else:
        print(f'{tc} Lose')