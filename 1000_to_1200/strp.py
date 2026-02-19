# Question Link: https://www.codechef.com/problems/STRP

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    while count < len(s)-1:
        if s[count] == s[count+1]:
            count += 2
            n -= 1
        else:
            count += 1
    print(n)