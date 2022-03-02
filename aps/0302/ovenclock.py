# 2525. 오븐 시계  2022-03-03

T, M = map(int, input().split())
N = int(input())

M += N
while M >= 60:
    T += 1
    M -= 60

while T >= 24:
    T -= 24

print(T, M)