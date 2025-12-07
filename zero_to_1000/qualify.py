# Question Link: https://www.codechef.com/problems/QUALIFY

# cook your dish here
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    tot = a + 2 * b
    if tot >= n:
        print("Qualify")
    else:
        print("NotQualify")