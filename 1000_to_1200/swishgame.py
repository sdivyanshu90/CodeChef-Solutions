# Question Link: https://www.codechef.com/problems/SWISHGAME

# cook your dish here
for _ in range(int(input())):
    m, k = map(int, input().split())
    s = input()
    
    count_S = s.count('S')
    
    if count_S >= k:
        print(m)
    else:
        print(m + (k - count_S - 1))