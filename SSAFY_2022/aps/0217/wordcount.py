T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    result = 0

    # str1의 글자 개수만큼 str2에서 찾아서 세기
    for i in range(len(str1)):
        cnt = 0
        for j in str2:
            if str1[i] == j:
                cnt += 1
        if cnt > result:
            result = cnt

    print(f'#{tc} {result}')
