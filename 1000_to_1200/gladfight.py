# cook your dish here
for _ in range(int(input())):
    n = int(input())
    maxSum = (n - 1) * (n - 2) // 2
    minSum = max(0, n - 2)
    print(minSum, maxSum)