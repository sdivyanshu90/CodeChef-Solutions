# Question Link: https://www.codechef.com/problems/WINNERR

# cook your dish here
for _ in range(int(input())):
    pa, pb, qa, qb = map(int, input().split())
    p = max(pa, pb)
    q = max(qa, qb)
    if p > q:
        print("Q")
    elif q > p:
        print("P")
    else:
        print("TIE")