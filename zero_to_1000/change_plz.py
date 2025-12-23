# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n % 10 == 0:
        print(100 - n)
    else:
        print(((100 - n) // 10) * 10)