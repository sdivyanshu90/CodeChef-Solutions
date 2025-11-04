# Question Link: https://www.codechef.com/problems/TASTEDEC

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    choco = 2 * x
    candy = 5 * y
    if choco > candy:
        print("Chocolate")
    elif candy > choco:
        print("Candy")
    else:
        print("Either")