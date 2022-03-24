T = int(input())
for tc in range(1, T+1):
    N, H = input().split()
    print(f'#{tc}', end=' ')
    for i in H:
        print(f'{int(i, 16):04b}', end="")
    print()