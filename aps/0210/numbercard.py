T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = str(input())
    cards = []

    for n in nums:
        cards += n
    cards = list(map(int, cards))


    cnt = [0] * 10
    for card in cards:
        cnt[card] += 1

    max_n = 0
    max_v = 0
    for i in range(10):
        if cnt[i] >= max_n:
            max_n = cnt[i]
            max_v = i

    print(f'#{tc} {max_v} {max_n}')
