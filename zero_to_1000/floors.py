# Question Link: https://www.codechef.com/problems/FLOORS

# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    floor_a = (a - 1) // 10 + 1
    floor_b = (b - 1) // 10 + 1
    print(abs(floor_a - floor_b))