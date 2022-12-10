T = 10
for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    gap = 0

    for i in range(dump):     # dump 횟수만큼 반복
        highest = boxes[0]
        lowest = boxes[0]
        for j in range(100):  # 가로 길이는 100으로 고정, 최대와 최소 먼저 구함
            if boxes[j] > highest:
                highest = boxes[j]
            if boxes[j] < lowest:
                lowest = boxes[j]

        for j in range(100):    # boxes 중 최대와 같은 값을 찾을 경우 -1
            if boxes[j] == highest:
                boxes[j] -= 1
                break

        for j in range(100):    # 최소와 같은 값에는 +1
            if boxes[j] == lowest:
                boxes[j] += 1
                break

        if highest in boxes and lowest in boxes:    # dump 이후 경우의수에 따른 gap
            gap = highest - lowest
        elif highest not in boxes and lowest not in boxes:
            gap = highest - lowest -2
        else:
            gap = highest - lowest -1

        if gap <= 1:            # flatten 완료 경우 break
            break

    print(f'#{tc} {gap}')