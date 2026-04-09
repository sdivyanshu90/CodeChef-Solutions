# Question Link: https://www.codechef.com/problems/ARRAYRET

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    
    s = sum(b)
    divisor = s // (n + 1)
    l = [x - divisor for x in b]
    print(*l)