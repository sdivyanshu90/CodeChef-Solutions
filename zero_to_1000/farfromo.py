# cook your dish here
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    bob = ((x2 ** 2) + (y2 ** 2)) ** 0.5
    alex = ((x1 ** 2) + (y1 ** 2)) ** 0.5
    if alex > bob:
        print("ALEX")
    elif bob > alex:
        print("BOB")
    else:
        print("EQUAL")