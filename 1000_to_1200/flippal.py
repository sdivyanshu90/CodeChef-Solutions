# Question Link: https://www.codechef.com/problems/FLIPPAL

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    
    count_1 = s.count('1')
    count_0 = n - count_1

    if count_1 % 2 != 0 and count_0 % 2 != 0:
        print("NO")
    else:
        print("YES")