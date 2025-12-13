# Question Link: https://www.codechef.com/problems/FILLCANDIES

# cook your dish here
for _ in range(int(input())):
    candies, pockets, pocket_capacity = map(int, input().split())
    # print(f"Candies: {candies}, No. of Pockets: {pockets}, Each Pocket Candy Capacity: {pocket_capacity}")
    part1 = pockets * pocket_capacity
    if candies % part1 == 0:
        print(candies // part1)
    else:
        print(candies // part1 + 1)