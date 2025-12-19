# Question Link: https://www.codechef.com/problems/AGENTCHEF

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = 0.2 * n
    if 100 % a == 0:
        print(int(100 // a))
    else:
        print(int((100 // a) + 1))