# Question Link: https://www.codechef.com/problems/CRDGAME

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    chef, morty = 0, 0
    for _ in range(n):
        a, b = map(int, input().split())
        scorea = scoreb = 0
        if a > 9:
            for dig in str(a):
                scorea += int(dig)
        else:
            scorea += a
                
        if b > 9:
            for dig in str(b):
                scoreb += int(dig)
        else:
            scoreb += b
                
        if scorea > scoreb:
            chef += 1
        elif scoreb > scorea:
            morty += 1
        else:
            chef += 1
            morty += 1
        
    if chef > morty:
        print(0, chef)
    elif morty > chef:
        print(1, morty)
    else:
        print(2, chef)