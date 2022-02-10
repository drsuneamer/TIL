T = int(input())
for tc in range(1, T+1):
    num = int(input())
    c = [0] * 12

    for i in range(6):
        c[num % 10] += 1
        num //= 10

    i = 0
    tri = runs = 0
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            runs += 1
            continue
        i += 1

    if runs + tri == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
