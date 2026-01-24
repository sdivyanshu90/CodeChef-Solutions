# cook your dish here
for _ in range(int(input())):
    x = int(input())
    s = input()
    draw, carl, chef = 0, 0, 0
    for char in s:
        if char == "C":
            carl += 2
        elif char == "D":
            chef += 1
            carl += 1
        else:
            chef += 2
    
    if carl > chef:
        print(60*x)
    elif carl == chef:
        print(55*x)
    else:
        print(40*x)