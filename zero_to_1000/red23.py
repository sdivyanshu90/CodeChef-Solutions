# Question Link: https://www.codechef.com/problems/RED23

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    while n > 0:
        if n % 2 == 0:
            n //= 2
        elif n > 3:
            n -= 3
        else:
            break
    print(n)