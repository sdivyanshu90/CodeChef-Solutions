# Question Link: https://www.codechef.com/problems/AIRHOCKEY

# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(7 - a)
    else:
        if a > b:
            print(7 - a)
        else:
            print(7 - b)