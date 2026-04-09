# Question Link: https://www.codechef.com/problems/BURGERS2

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    count_even = sum(1 for i in a if i % 2 == 0)
    print(0 if count_even == n else count_even)