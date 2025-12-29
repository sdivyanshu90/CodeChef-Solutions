# Question Link: https://www.codechef.com/problems/PRB01

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    
    if prime and n != 1:
        print("yes")
    else:
        print("no")