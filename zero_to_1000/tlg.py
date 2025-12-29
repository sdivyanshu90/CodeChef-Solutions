# Question Link: https://www.codechef.com/problems/TLG

# cook your dish here
rounds = []
for _ in range(int(input())):
    p1, p2 = map(int, input().split())
    rounds.append([p1, p2])

res = []
cum_p1 = 0
cum_p2 = 0

for p1, p2 in rounds:
    cum_p1 += p1
    cum_p2 += p2
    
    if cum_p1 > cum_p2:
        res.append((1, (cum_p1 - cum_p2)))
    else:
        res.append((2, (cum_p2 - cum_p1)))
        
print(*max(res, key = lambda x: x[1]))