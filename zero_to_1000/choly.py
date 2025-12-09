# Question Link: https://www.codechef.com/problems/CHOLY

# cook your dish here
win, draw, loss = map(int, input().split())
first = 1 * win + draw * 0.5
second = 1 * loss + draw * 0.5
if first +  (4 - (win + draw + loss)) > second:
    print("Yes")
else:
    print("No")