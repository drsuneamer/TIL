T = int(input())
for tc in range(1, T+1):
    str1 = input()  # 패턴
    str2 = input()  # 문자열
    N = 0   # 패턴 길이
    M = 0   # 문자열 길이

    for i in str1: N += 1
    for i in str2: M += 1

    i = 0   # 문자열의 인덱스
    j = 0   # 패턴의 인덱스

    while i < M and j < N:
        if str2[i] != str1[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == N:
            print(1)
            break       # 문자열을 찾으면(str1의 마지막 인덱스) 1 출력 후 종료
    else:
        print(0)