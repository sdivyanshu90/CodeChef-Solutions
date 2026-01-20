# Question Link: https://www.codechef.com/problems/SHOEFIT

# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    zero = 0
    one = 0
    for num in a:
        if num == 0:
            zero += 1
        else:
            one += 1
    if zero >= 1 and one >= 1:
        print(1)
    else:
        print(0)