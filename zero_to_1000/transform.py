# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n % 3 == 1:
        print("HUGE")
    elif n % 3 == 2:
        print("SMALL")
    else:
        print("NORMAL")