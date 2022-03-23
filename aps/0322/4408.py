T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * 401
    for i in range(N):
        a, b = map(int, input().split())
        if a < b:
            for j in range(a, b+1):
                lst[j] += 1
        else:
            for j in range(b, a+1):
                lst[j] += 1

    print(f'#{tc} {max(lst)}')
