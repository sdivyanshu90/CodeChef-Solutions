# Question Link: https://www.codechef.com/problems/FCTRL

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    count = 0
    while n > 0:
        n //= 5
        count += n
    print(count)