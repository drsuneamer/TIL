#### 순열

```python
def perm(i, N):
    # 전체 칸 다 완성하면 print
    if i == N:
        print(A)
    else:
        # fix되지 않은 부분 바꾸면서 진행
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            perm(i+1, N)
            A[j], A[i] = A[i], A[j]
            
        
A = [1, 2, 3]
N = len(A)
perm(0, N)
```



#### 조합 (DFS 사용)

```python
def DFS(Level, BeginWith):
    
    if Level == r:
        print(result)
    else:
        for i in range(BeginWith, len(n)):
            result[Level] = n[i]
            DFS(Level + 1, i + 1)
     
# nCr
n = [1, 2, 3]
r = 2
result = [0] * r

DFS(0, 0)
```





#### DFS

```python
def dfs(i, j):
    # 목적지 찾으면 return
    if maze[i][j] == 3:
        return 1
    else:
        maze[i][j] = 1		# 진입한 칸을 벽으로 메꿈
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                if dfs(ni, nj):
                    return 1
        return 0	# 현재 칸으로부터 이동 후 도착점을 찾지 못하면
```



#### DFS - stack

````python
def dfs_stack(i, j):
    stack = []
    visited = [[0] * N for _ in range(N)]
    stack.append((i, j))	# 시작점 push
    visited[i][j] = 1
    while stack:
        i, j = stack.pop()
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < 16 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                stack.append((ni, nj))
                visited[ni][nj] = 1
    return 0
````



### 2차원 배열 정렬

> https://asxpyn.tistory.com/75

```python
arr = [[2, 3], [1, 2], [0, 4]]
# 두번째 값 기준으로 오름차순 정렬
arr.sort(key = lambda x:x[1])
arr = [[1, 2], [2, 3], [0, 4]]
```



### 소수점 이하 자릿수 맞추기

>https://outofgreed.tistory.com/312

```python
score = '{:.2f}'.format(round(x,2))
# 8.50 (두번째 자리 채워짐)
```



### 에라토스테네스의 체

> https://wikidocs.net/21638

1. 1은 제거
2. 지워지지 않은 수 중 가장 작은 수인 2를 소수로 채택하고, 2의 배수를 모두 지운다
3. 지워지지 않은 수 중 가장 작은 수인 3을 소수로 채택하고, 3의 배수를 모두 지운다.
4. 지워지지 않은 수 중 가장 작은 수인 5를 소수로 ...

```python
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [1] * (n + 1)

    m = int(n ** 0.5)  # n의 최대 약수는 sqrt(n) 이하
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = 0

    return [x for x in range(2, n + 1) if sieve[x] == 1]
```

