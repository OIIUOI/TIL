# DFS

## Recursive code

```python
visit = [False] * n

graph = [[], [], [], []]

def dfs(start):
    visit[start] = True

    for adj in graph[start]
        if not visit[adj]:
            dfs(adj)
```

## Code

```python
visit = [False] * n

graph = [[], [], [], []]


def dfs(start):
    visit[start] = True
    stack = [start]

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visit[adj]:
                visit[adj] = True
                stack.append(adj)
```

# BFS

## Code

```python
from collections import deque

visit = [False] * n

graph = [[], [], [], []]

def bfs(start):
    queue = deque([start])
    visit[start] = True


    while queue:
        cur = queue.popleft()

        for adj in graph[cur]:
            if not visited[adj]:
                queue.append(adj)
                visit[adj] = True
```
