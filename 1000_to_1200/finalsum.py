# Question Link: https://www.codechef.com/problems/FINALSUM

# cook your dish here
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    res = sum(a)
    for _ in range(q):
        l, r = map(int, input().split())
        d = r - l + 1
        if d % 2 != 0:
            res += 1
    print(res)