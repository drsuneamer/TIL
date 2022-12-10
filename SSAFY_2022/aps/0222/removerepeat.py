T = int(input())
for tc in range(1, T+1):
    a = input()
    size = len(a)
    stack = [''] * size
    top = 0
    stack[0] = a[0]

    for i in range(1, size):
        if stack[top] == a[i]:
            top -= 1
        else:
            top += 1
            stack[top] = a[i]

    print(f'#{tc}', top + 1)