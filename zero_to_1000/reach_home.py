# Question Link: https://www.codechef.com/problems/REACH_HOME

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x * 5 >= y:
        print("YES")
    else:
        print("NO")