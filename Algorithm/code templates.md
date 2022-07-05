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

