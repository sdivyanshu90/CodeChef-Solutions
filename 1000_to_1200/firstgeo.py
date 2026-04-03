# Question Link: https://www.codechef.com/problems/FIRSTGEO

# cook your dish here
for _ in range(int(input())):
    s = input()
    
    x = 1 + 10 * s[:2].count('1')
    y = 1 + 10 * s[2:].count('1')
    print(x * y)