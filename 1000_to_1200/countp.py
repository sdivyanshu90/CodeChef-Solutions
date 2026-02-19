# Question Link: https://www.codechef.com/problems/COUNTP

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    count = sum(1 for i in array if i % 2 == 1)
    if count % 2 == 1 or count == 0:
        print("NO")
    else:
        print("YES")