T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    
    for i in range(N-1, 0, -1):     # 전체 버블 정렬
        for j in range(0, i):
            if ai[j] > ai[j+1]:
                ai[j], ai[j+1] = ai[j+1], ai[j]

    a = [0] * N     # 정답 리스트
    for i in range(N//2):   # 작은 수부터 짝수 인덱스에
        a[i*2+1] = ai[i]

    for i in range(N-1, N//2-1, -1):    # 큰 수부터 홀수 인덱스에
        a[2*(N-1-i)] = ai[i]

    print(f'#{tc}', end=' ')    # 10개까지 출력
    for i in range(10):
        print(a[i], end=' ')
    print()