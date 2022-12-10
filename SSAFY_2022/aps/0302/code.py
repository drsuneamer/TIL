T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    front = rear = 0
    print(arr)

    while arr[rear] >= 0:
        arr[rear] -= 1
        rear = (rear + 1) % 8
