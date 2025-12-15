# Question Link: https://www.codechef.com/problems/SMLPAL

# cook your dish here
for _ in range(int(input())):
    ones, twos = map(int, input().split())
    first_half = '1' * (ones // 2) + '2' * (twos // 2)
    print(first_half + first_half[::-1])