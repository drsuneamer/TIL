T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans = 0

    for n in B:
        key = n
        L = 0
        R = N - 1
        c = ''  # 번갈아서 가는지 확인
        while L <= R:
            middle = (L + R) // 2
            if A[middle] == key:
                c = ''
                ans += 1
                break
            elif A[middle] > key:
                if c == 'L':
                    break
                c = 'L'
                R = middle - 1
            else:
                if c == 'R':
                    break
                c = 'R'
                L = middle + 1

    print(f'#{tc} {ans}')



