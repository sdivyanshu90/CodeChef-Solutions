# Question Link: https://www.codechef.com/problems/CHEFGAMES

# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    if sum(a) == 0:
        print("IN")
    else:
        print("OUT")