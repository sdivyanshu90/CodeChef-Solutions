# cook your dish here
for _ in range(int(input())):
    r = int(input())
    if 1000 <= r < 1600:
        print(3)
    elif 1600 <= r < 2000:
        print(2)
    else:
        print(1)