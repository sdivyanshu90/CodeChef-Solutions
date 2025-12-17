# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    salary = 2 ** x
    res = salary
    if n == 1:
        res = salary - (salary // 2)
    else:
        while n > 0:
            res -= res // 2
            n -= 1
            
    print(res)