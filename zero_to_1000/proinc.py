# Question Link: https://www.codechef.com/problems/PROINC

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    buy = x - y
    increment = int(x * 0.1)
    new_price = x + increment
    print(new_price - buy)