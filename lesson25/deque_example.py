from collections import deque

a = deque([1,4,6,9,3,'j'])
a.append(5)
a.append('h')
a.appendleft('o')
print(a)
a.rotate(1)
print(a)
b = list(a)
print(b)