# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n % 5 != 0 and n % 10 != 0:
        print(-1)
    else:
        res = 0
        while n > 0:
            if n >= 10:
                n -= 10
            else:
                n -= 5
            res += 1
            
        print(res)