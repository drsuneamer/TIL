def win(a, b):
    # 가위: 1, 바위: 2, 보: 3
    if (L[a-1] == 1 and L[b-1] == 2) or (L[a-1] == 2 and L[b-1] == 3) or (L[a-1] == 3 and L[b-1] == 1):
        return b
    else:   # 비기면 수가 작은 왼쪽 return
        return a


def f(i, j):
    if i == j:
        return i
    else:
        a = f(i, (i+j)//2)
        b = f((i+j)//2+1, j)
        return win(a, b)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    print(f'#{tc}', f(1, N))
