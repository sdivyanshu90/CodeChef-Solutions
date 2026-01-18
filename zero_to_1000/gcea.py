# Question Link: https://www.codechef.com/problems/GCEA

# cook your dish here
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    master = 0
    normal = 0
    res = 0
    for poke in a:
        normal = (x*poke)
        master = y
        res += min(normal, master)
            
    print(res)