# Question Link: https://www.codechef.com/problems/INCREAR

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())

    if x <= y:
        print(y - x)
    else:
        d = x - y
        if d % 2 == 0:
            print(d // 2)
        else:
            print((d + 3) // 2)