# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n in list(range(1, 11)):
        print("LOWER DOUBLE")
    elif n in [11, 12, 13, 14, 15]:
        print("LOWER SINGLE")
    elif n in list(range(16, 26)):
        print("UPPER DOUBLE")
    else:
        print("UPPER SINGLE")