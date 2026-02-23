# Question: https://www.codechef.com/START11B/problems/GRPASSN

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    peoples = set(p)
    for i in peoples:
        if p.count(i) % i != 0:
            print("NO")
            break
    else:
        print("YES")