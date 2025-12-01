# Question Link: https://www.codechef.com/problems/CHEAPFOOD

# cook your dish here
for _ in range(int(input())):
    x = int(input())
    coup1 = round(0.1 * x)
    coup2 = 100
    if coup1 > coup2:
        print(coup1)
    else:
        print(coup2)