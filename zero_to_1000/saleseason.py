# Question Link: https://www.codechef.com/problems/SALESEASON

# cook your dish here
for _ in range(int(input())):
    x = int(input())
    discount = 0
    if x <= 100:
        discount = 0
    elif 100 < x <= 1000:
        discount = 25
    elif 1000 < x <= 5000:
        discount = 100
    else:
        discount = 500
        
    print(x - discount)