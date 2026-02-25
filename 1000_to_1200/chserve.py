# Question Link: https://www.codechef.com/problems/CHSERVE

# cook your dish here
for _ in range(int(input())):
    chef, cook, k = map(int, input().split())
    blocks = (chef + cook) // k
    if blocks % 2 == 0:
        print("CHEF")
    else:
        print("COOK")