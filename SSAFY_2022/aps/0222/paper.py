T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10

    def paper(n):
        f = [0] * n
        f[0] = 1
        f[1] = 3

        for i in range(2, n):
            f[i] = f[i-1] + 2*f[i-2]

        return f[n-1]

    print(f'#{tc}', paper(N))