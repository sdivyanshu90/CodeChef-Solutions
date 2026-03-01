# Question Link: https://www.codechef.com/problems/PLAYSTR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    r = input()
    zero_s, one_s, zero_r, one_r = s.count("0"), s.count("1"), r.count("0"), r.count("1")
    
    if zero_r == zero_s and one_s == one_r:
        print("YES")
    else:
        print("NO")