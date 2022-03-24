## DFS / BFS

> 그래프 탐색 알고리즘



- 탐색(Search)

  많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

  

### Stack

- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
- **입구와 출구가 동일한 형태**로 시각화할 수 있다.



### Que

- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- **입구와 출구가 모두 뚫려 있는 터널과 같은 형태**로 시각화
- 시간 절약을 위해서는 deque를 이용하는 것이 유리하다



#### deque

```python
from collections import deque
queue = deque()
```

```python
import collections
deq = collections.deque(['a', 'b', 'c'])
```



- Deque(데크)란 double-ended queue의 줄임말로, 앞과 뒤에서 즉 양방향에서 데이터를 처리할 수 있는 queue형 자료를 의미한다. 

  ![image-20220325001008085](C:\Users\drsuneamer\AppData\Roaming\Typora\typora-user-images\image-20220325001008085.png)

- deque의 메소드들

  - `append(x)`

    list.append(x)와 마찬가지로 오른쪽(마지막)에 추가(삽입)

  - `appendleft(x)`

    왼쪽, 즉 앞쪽에서 추가(삽입)

  - `extend(iterable)`

    iterable argument를 오른쪽(마지막)에 하나씩 추가

  - `extendleft(iterable)`

    왼쪽(앞쪽)에서 데이터 추가(삽입)

  - `pop()`

    오른쪽(마지막)에서부터 차례대로 제거와 반환(remove and return)

  - `popleft()`

    왼쪽(앞쪽)에서부터 차례대로 제거와 반환(remove and return)

  - `rotate(n)`

    요소들을 값만큼 회전해준다. 음수이면 왼쪽으로, 양수이면 오른쪽으로 회전

    ```python
    import collections
    
    deq = collections.deque(['a', 'b', 'c', 'd', 'e'])
    deq.rotate(1)
    print('deq >>', ' '.join(deq))	# deq >> e a b c d
    
    deq2 = collections.deque(['a', 'b', 'c', 'd', 'e'])
    deq2.rotate(2)
    print('deq2 >>', ' '.join(deq2))	# deq2 >> d e a b c
    
    deq3 = collections.deque(['a', 'b', 'c', 'd', 'e'])
    deq3.rotate(-1)
    print('deq3 >>', ' '.join(deq3))	# deq3 >> b c d e a
    
    deq4 = collections.deque(['a', 'b', 'c', 'd', 'e'])
    deq4.rotate(-2)
    print('deq4 >>', ' '.join(deq4))	# deq4 >> c d e a b
    
    ```

    

### 재귀함수

- 재귀함수(Recursive Function)란 **자기 자신을 다시 호출하는 함수**를 의미한다.

- 재귀함수를 문제풀이에서 사용할 때는 재귀함수의 종료 조건을 반드시 명시해야 한다. 그렇지 않을 경우 무한히 호출될 수 있다.

  - 종료 조건을 포함한 재귀 함수 예제

    ```python
    def recursive_function(i):
        # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
        if i == 100:
            return
        print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
        recursive_function(i+1)
        print(i, '번째 재귀함수를 종료합니다.')
    
    recursive_function(1)
    ```

    

- 재귀함수 예시 - 유클리드 호제법

  - 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 하자.

  - 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

    ```python
    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
        
    print(gcd(192, 162))
    ```

    

### DFS

> Depth-First Search

- DFS는 **깊이 우선 탐색**이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
- DFS는 **스택 자료구조(혹은 재귀 함수)**를 이용하며, 구체적인 동작 과정은 다음과 같다.
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.