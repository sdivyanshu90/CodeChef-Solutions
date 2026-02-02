# cook your dish here
for i in range(int(input())):
    n = int(input())
    s = input()
    server = 0
    alice = 0
    bob = 0
    for j in range(n):
        if (server == 0) and (s[j] == 'A'):
            alice += 1
        elif (server == 0) and (s[j] == 'B'):
            server = 1
        elif (server == 1) and (s[j] == 'B'):
            bob += 1
        else:
            server = 0
    print(alice, bob)