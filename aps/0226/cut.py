T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    stick = 0   # 현재 있는 쇠막대기의 수
    ans = 0     # 출력할 결과 값 (잘려진 조각의 총 개수)

    for i in range(len(lst)):
        if lst[i] == '(':
            stick += 1  # 여는 괄호: 쇠막대 추가
        else:  # 닫는 괄호 만날 경우
            # 이전이 여는 괄호였던 경우 : 레이저
            if lst[i-1] == '(':
                stick -= 1  # 이전 괄호로 추가된 막대 개수 빼고
                ans += stick    # 현재 있는 막대 개수만큼 추가
            else:   # 이전이 여는 괄호가 아닌 경우: 그냥 막대가 끝난 것 (잘린 조각 하나 추가)
                stick -= 1
                ans += 1

    print(f'#{tc} {ans}')
