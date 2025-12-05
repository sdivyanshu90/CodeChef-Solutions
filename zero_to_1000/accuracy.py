# cook your dish here
for _ in range(int(input())):
    x = int(input())
    if x % 3 == 0:
        print(0)
    elif x % 3 == 2:
        print(1)
    else:
        print(2)