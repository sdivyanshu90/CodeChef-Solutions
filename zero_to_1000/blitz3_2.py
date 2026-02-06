# Question Link: https://www.codechef.com/problems/BLITZ3_2

# cook your dish here
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    total_time = 2 * (180 + n)
    print(total_time - (a + b))