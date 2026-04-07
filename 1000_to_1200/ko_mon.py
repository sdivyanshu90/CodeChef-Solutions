# Question Link: https://www.codechef.com/problems/KO_MON

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    monster_strengths = list(map(int, input().split()))
    
    monster_strengths.sort(reverse=True)
    power = monster_strengths[0]
    for idx in range(1, n):
        power = max(power, monster_strengths[idx] + idx * x)
    print(power)