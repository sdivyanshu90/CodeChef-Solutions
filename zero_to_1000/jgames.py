# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
        print("Janmansh")
    else:
        print("Jay")