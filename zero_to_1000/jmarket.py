# Question Link: https://www.codechef.com/problems/JMARKET

# cook your dish here
for _ in range(int(input())):
    x, a, b, c = map(int, input().split())
    mini = min(a, b, c)
    second_mini = 0
    if a <= b <= c or c <= b <= a:
        second_mini = b
    elif b <= a <= c or c <= a <= b:
        second_mini = a
    else:
        second_mini = c
    print(mini * (x - 1) + second_mini)