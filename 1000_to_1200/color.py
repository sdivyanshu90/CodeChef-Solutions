# Question Link: https://www.codechef.com/problems/COLOR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    counts = [s.count(i) for i in set(s)]
    print(n - max(counts))