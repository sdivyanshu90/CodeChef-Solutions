# Question Link: https://www.codechef.com/problems/SEVENRINGS

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    number = str(n * x)
    if number[0] != "0" and len(number) == 5:
        print("YES")
    else:
        print("NO")