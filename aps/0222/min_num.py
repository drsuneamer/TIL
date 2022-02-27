T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    min_v = 1e+10       # 비교할 가장 큰 수
    min_i = 0           # 현재 가장 큰 수의 인덱스

    for i in range(N):
        if L[i] < min_v:
            min_v = L[i]
            min_i = i

    print(f'#{tc} {min_i+1}')   # 인덱스값에 1을 더해서 위치 출력