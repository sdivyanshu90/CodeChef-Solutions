# Question Link: https://www.codechef.com/problems/PERMOR

# cook your dish here
for _ in range(int(input())):
    N = int(input())
    permutation = list(range(1, N + 1))
    for i in range(2, N, 2):
        permutation[i], permutation[i - 1] = permutation[i - 1], permutation[i]
    print(" ".join(map(str, permutation)))