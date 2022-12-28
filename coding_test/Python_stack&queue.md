# Python

---

## Stack

![](C:\Users\jin47\OneDrive\바탕%20화면\TIL\coding_test\asset\2022-12-28-11-39-42-image.png)

```python
s = []

s.append(5)
s.append(2)
s.append(3)
s.append(4)
s.pop()
s.append(1)

print(s[::-1])
# [1,3,2,5]
```



---

## Queue

![](C:\Users\jin47\OneDrive\바탕%20화면\TIL\coding_test\asset\2022-12-28-11-43-51-image.png)

```python
from collections import deque


q = deque()

q.append(5) # 5
q.append(2) # 2 5
q.append(3) # 3 2 5
q.append(7) # 7 3 2 5
q.popleft() # 7 3 2
q.append(1) # 1 7 3 2
q.append(4) # 4 1 7 3 2
q.popleft() # 4 1 7 3

print(q) # [3,7,1,4]
q.reverse()
print(q) # [4,1,7,3]
```
