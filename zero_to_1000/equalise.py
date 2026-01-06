# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())

    while a % 2 == 0:
        a //= 2
    while b % 2 == 0:
        b //= 2

    if a == b:
        print("YES")
    else:
        print("NO")