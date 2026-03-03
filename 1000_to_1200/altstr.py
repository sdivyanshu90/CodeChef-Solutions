# Question Link: https://www.codechef.com/problems/ALTSTR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    
    c0 = s.count("0")
    c1 = s.count("1")
    
    print(min(n, 2 * min(c0, c1) + 1))