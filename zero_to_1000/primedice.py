# Question Link: https://www.codechef.com/problems/PRIMEDICE

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    tot = x + y
    prime = True
    for i in range(2, int(tot ** 0.5) + 1):
        if tot % i == 0:
            prime = False
    if prime:
        print("Alice")
    else:
        print("Bob")