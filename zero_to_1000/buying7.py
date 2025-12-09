# Question Link: https://www.codechef.com/problems/BUYING7

# cook your dish here
for _ in range(int(input())):
    k, n = map(int, input().split())
    c = list(map(int, input().split()))
    c.sort(reverse = True)
    print(sum(c[:n]))