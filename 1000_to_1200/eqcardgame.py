# Question Link: https://www.codechef.com/problems/EQCARDGAME

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    eq = 52 // n
    # print(52 // n)
    print(52 - (n * eq))