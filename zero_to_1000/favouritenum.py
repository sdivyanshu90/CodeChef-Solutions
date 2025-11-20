# Question Link: https://www.codechef.com/problems/FAVOURITENUM

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0 and n % 7 == 0:
        print("Alice")
    elif n % 2 != 0 and n % 9 == 0:
        print("Bob")
    else:
        print("Charlie")