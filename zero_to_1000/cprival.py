# Question Link: https://www.codechef.com/problems/CPRIVAL

# cook your dish here
r1, r2 = map(int, input().split())
d1, d2 = map(int, input().split())

dom_rate = r1 + d1
eve_rate = r2 + d2

if dom_rate > eve_rate:
    print("Dominater")
else:
    print("Everule")