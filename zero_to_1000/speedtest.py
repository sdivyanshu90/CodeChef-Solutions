# cook your dish here
for _ in range(int(input())):
    a, x, b, y = map(int, input().split())
    al = a / x
    bo = b / y
    if al > bo:
        print("Alice")
    elif bo > al:
        print("Bob")
    else:
        print("Equal")