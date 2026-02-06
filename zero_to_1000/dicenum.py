# Question Link: https://www.codechef.com/problems/DICENUM

# cook your dish here
for _ in range(int(input())):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    a = [a1, a2, a3]
    b = [b1, b2, b3]
    a.sort(reverse = True)
    b.sort(reverse = True)
    alice = int("".join(map(str, a)))
    bob = int("".join(map(str, b)))
    # print(alice, bob)
    if alice == bob:
        print("Tie")
    elif alice > bob:
        print("Alice")
    else:
        print("Bob")