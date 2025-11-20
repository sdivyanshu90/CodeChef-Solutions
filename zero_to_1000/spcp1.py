# Question Link: https://www.codechef.com/problems/SPCP1

# cook your dish here
chef_height, chef_weight = 130, 60
w, h = map(int, input().split())

if chef_height >= h and  chef_weight <= w:
    print("YES")
else:
    print("NO")