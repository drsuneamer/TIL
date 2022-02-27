T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    route = [0] * 201

    for i in range(N):
        start, end = map(int, input().split())
        if start % 2 == 0:
            if end % 2 == 0:    # 짝 짝
                for j in range(start, end + 1, 2):
                    route[j // 2] += 1
            else:               # 짝 홀
                for j in range(start, end + 2, 2):
                    route[j // 2] += 1
        else:
            for j in range(start, end + 1, 2):
                route[j // 2 + 1] += 1
    print(route)
    # for i in route:
    #     if i > ans:
    #         ans = i
    #
    # print(f'#{tc} {ans}')