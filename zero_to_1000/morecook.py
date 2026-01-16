# Question Link: https://www.codechef.com/problems/MORECOOK

# cook your dish here
for _ in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    
    a_set = set(a)
    if c not in a_set and any(i < c for i in a):
        print(0)
        continue
    
    res = 1
    while True:
        temp = c + res
        if temp not in a_set and any(i < temp for i in a):
            print(res)
            break
        res += 1