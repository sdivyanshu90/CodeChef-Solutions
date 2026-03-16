# Question Link: https://www.codechef.com/problems/GAMEOFPILES1

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if 1 in a:
        print('CHEF')
    elif a.count(2) == n:
        print('CHEFINA')
    else:
        score = sum(i - 2 for i in a if i > 2)
        print('CHEFINA' if score % 2 == 0 else 'CHEF')