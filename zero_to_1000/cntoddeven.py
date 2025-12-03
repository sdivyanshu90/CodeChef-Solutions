# Question Link: https://www.codechef.com/problems/CNTOODDEVEN

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    odd, even = 0, 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
                
    print(odd, even)