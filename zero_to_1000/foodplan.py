# Question Link: https://www.codechef.com/problems/FOODPLAN

# cook your dish here
for _ in range(int(input())):
    online, offline = map(int, input().split())
    final_price = online - (0.1 * online)
    if final_price < offline:
        print("ONLINE")
    elif final_price > offline:
        print("DINING")
    else:
        print("EITHER")