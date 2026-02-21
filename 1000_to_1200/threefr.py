# Question Link: https://www.codechef.com/problems/THREEFR

# cook your dish here
for _ in range(int(input())):
    X, Y, Z = map(int, input().split())
    
    if X + Y == Z or Y + Z == X or Z + X == Y:
        print("YES")
    else:
        print("NO")