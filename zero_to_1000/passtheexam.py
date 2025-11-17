# Question Link: https://www.codechef.com/problems/PASSTHEEXAM

# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    tot = a + b + c
    
    if (a >= 10 and b >= 10 and c >= 10) and tot >= 100:
        print("PASS")
    else:
        print("FAIL")