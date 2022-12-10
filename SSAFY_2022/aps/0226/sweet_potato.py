T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    how_many = 0    # 긴 줄기의 수
    now_longest = 0 # 현재 가장 긴 줄기
    most_ko = 0     # 현재 가장 긴 줄기의 고구마 수

    cnt = ko = 0    # cnt = 줄기의 길이 - 1 (비교만 하기때문에 굳이 1 더해줄 필요 X) / ko = 고구마 개수
    for i in range(1, N):   # 두번째 값부터 확인
        if L[i] > L[i-1]:
            cnt += 1
            if cnt == 1:    # 긴 줄기인 것이 확인되면 개수 추가, 더해지지 않은 앞의 값도 더해줌
                how_many += 1
                ko += L[i-1]
            ko += L[i]

        else:
            if cnt > now_longest:   # 가장 긴 줄기인 것이 확인되면 값 변경
                now_longest = cnt
                most_ko = ko
            if cnt == now_longest:  # 가장 긴 줄기가 여럿이면 고구마가 많은 쪽
                if ko > most_ko:
                    most_ko = ko
            cnt = ko = 0    # 줄기와 고구마 모두 초기화

    # 마지막까지 이어진 줄기가 가장 긴 줄기였을 경우
    if cnt > now_longest:
        most_ko = ko
    if cnt == now_longest:
        if ko > most_ko:
            most_ko = ko

    print(f'#{tc} {how_many} {most_ko}')