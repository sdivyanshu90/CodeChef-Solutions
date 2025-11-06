# Question Link: https://www.codechef.com/problems/FINE

# cook your dish here
for _ in range(int(input())):
    x = int(input())
    if x > 100:
        print(2000)
    elif x > 70 and x <= 100:
        print(500)
    else:
        print(0)