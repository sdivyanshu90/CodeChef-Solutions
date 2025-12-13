# Question Link: https://www.codechef.com/problems/MYSERVE

# cook your dish here
for _ in range(int(input())):
    alice, bob = map(int, input().split())
    if ((alice + bob) // 2) % 2 == 0:
        print("Alice")
    else:
        print("Bob")