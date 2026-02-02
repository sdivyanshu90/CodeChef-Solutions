# Question Link: https://www.codechef.com/problems/MODULO3

# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    count = 0
    while (a % 3 != 0) and (b % 3 != 0):
        a, b = abs(a - b), min(a, b)
        count += 1
    print(count)