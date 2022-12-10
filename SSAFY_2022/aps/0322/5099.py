T = int(input())
for tc in range(1, T+1):
    # N: 화덕의 크기, M: 피자의 개수
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    oven = []
    idx = N
    for i in range(N):
        oven.append([i, C[i]])

    while oven:
        if len(oven) == 1:
            print(f'#{tc} {oven[0][0] +1}')
            break
        else:
            a = oven.pop(0)
            if a[1] // 2 == 0 and idx < M:
                oven.append([idx, C[idx]])
                idx += 1
            elif a[1] // 2 == 0 and idx >= M:
                pass
            else:
                a[1] //= 2
                oven.append(a)

