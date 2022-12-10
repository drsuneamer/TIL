N = int(input())    # 스위치 개수
switch = [0] + list(map(int, input().split())) # 스위치 상태
S = int(input())    # 학생 수

for i in range(S):
    # a = 학생의 성별(남1, 여2) b = 받은 숫자 (<N)
    a, b = map(int, input().split())
    # 남학생의 경우
    if a == 1:
        for num in range(1, len(switch)):
            if num % b == 0:    # 스위치 인덱스가 b의 배수인 경우
                if switch[num] == 1:
                    switch[num] = 0
                elif switch[num] == 0:
                    switch[num] = 1
    # 여학생의 경우
    else:
        if b <= len(switch) // 2:
            n = b - 1
            for num in range(1, n+1):
                if switch[b-num] == switch[b+num]:
                    if switch[b-num] == 1:
                        switch[b-num] = 0
                    elif switch[b-num] == 0:
                        switch[b-num] = 1
                    if switch[b+num] == 1:
                        switch[b+num] = 0
                    elif switch[b+num] == 0:
                        switch[b+num] = 1
                else:
                    break
            if switch[b] == 1:
                switch[b] = 0
            elif switch[b] == 0:
                switch[b] = 1

        else:
            n = len(switch) - b
            for num in range(1, n+1):
                if switch[b-num] == switch[b+num]:
                    if switch[b-num] == 1:
                        switch[b-num] = 0
                    elif switch[b-num] == 0:
                        switch[b-num] = 1
                    if switch[b+num] == 1:
                        switch[b+num] = 0
                    elif switch[b+num] == 0:
                        switch[b+num] = 1
                else:
                    break
            if switch[b] == 1:
                switch[b] = 0
            elif switch[b] == 0:
                switch[b] = 1

p = ((len(switch) -1) // 20) + 1
for k in range(p):
    try:
        for j in range((20*(p-1))+1, (20*(p+1))+1):
            print(switch[j], end=' ')
        print()
    except IndexError:
        break
