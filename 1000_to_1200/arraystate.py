# cook your dish here
from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = deque(map(int, input().split()))
    while k != 0:
        x = a.popleft()
        y = a.pop()
        a.append(x + y)
        k -= 1
    print(*a)