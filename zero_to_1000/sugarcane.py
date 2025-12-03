# Question Link: https://www.codechef.com/problems/SUGARCANE

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    tot_income = 50 * n
    profit = tot_income - round(tot_income * 0.7)
    print(profit)