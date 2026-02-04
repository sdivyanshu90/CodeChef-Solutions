# Question Link: https://www.codechef.com/problems/NAICHEF

# cook your dish here
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    x = list(map(int, input().split()))
    counta, countb = 0, 0
    for i in x:
        if i == a:
            counta += 1
    for i in x:
        if i == b:
            countb += 1
        
    print((counta * countb) / (n**2))