# [D2] 1983. 조교의 성적 매기기  2022-03-02

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    n = int(N / 10)
    G = ['0', 'D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
    grades = []

    for i in range(N):
        a, b, c = map(int, input().split())
        grades.append(a*0.35 + b*0.45 + c*0.2)

    n_grades = [0] + sorted(grades)
    for_result = {}

    for i in range(1, 11):
        for j in range((i-1)*n+1, i*n+1):
            if n_grades[j] in for_result:
                pass
            else:
                for_result[n_grades[j]] = G[i]

    print(f'#{tc}', for_result[grades[K-1]])

