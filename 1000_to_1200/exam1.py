# Question Link: https://www.codechef.com/problems/EXAM1

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    u = input()
    
    score = 0
    skip = False
    
    for i in range(n):
        if skip:
            skip = False
            continue
        
        if u[i] == s[i]:
            score += 1
        else:
            if u[i] != 'N':
                skip = True
    
    print(score)