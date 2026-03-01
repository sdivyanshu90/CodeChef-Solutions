# Question Link: https://www.codechef.com/problems/ORDDIST

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    p = y[0]
    order = sorted(range(n), key=lambda i: (abs(x[i] - p), x[i]))
    
    if all(y[i] == x[order[i]] for i in range(n)):
        print(order[0] + 1)
    else:
        print(-1)