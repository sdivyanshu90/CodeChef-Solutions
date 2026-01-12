# Question Link: https://www.codechef.com/problems/PRIMESUM7

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(str, input().split()))
    c1, c2, c3 = a.count('1'), a.count('2'), a.count('3')
    part1 = (c1 * (c1 - 1)) // 2
    part2 = c1 * c2 + c2 * c3
    print(part1 + part2)