# Question Link: https://www.codechef.com/problems/COCONUT

# cook your dish here
for _ in range(int(input())):
    xa, xb, needa, needb = map(int, input().split())
    typea = needa // xa
    typeb = needb // xb
    print(typea +  typeb)