# cook your dish here
for _ in range(int(input())):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())

    resa = a1 + a2 + a3 - min(a1, a2, a3)
    resb = b1 + b2 + b3 - min(b1, b2, b3)

    if resa > resb:
        print("Alice")
    elif resb > resa:
        print("Bob")
    else:
        print("Tie")