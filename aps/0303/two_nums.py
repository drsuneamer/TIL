# [D2] 1959. 두 개의 숫자열  2022-03-03

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0


    if M > N:
        n = M - N + 1
        for i in range(n):
            nA = [0]*i + A
            c = 0
            for j in range(len(nA)):
                c += nA[j] * B[j]
            if c > result:
                result = c

    else:
        n = N - M + 1
        for i in range(n):
            nB = [0]*i + B
            c = 0
            for j in range(len(nB)):
                c += A[j] * nB[j]
            if c > result:
                result = c

    print(f'#{tc} {result}')