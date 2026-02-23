# Question: https://www.codechef.com/problems/EQUALSTRING

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    unique = set()
    for i in range(n):
        if a[i] != b[i]:
            unique.add(b[i])
    print(len(unique))