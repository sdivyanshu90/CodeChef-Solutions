# Question Link: https://www.codechef.com/problems/MXON

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    
    for i in range(n - 2, -1, -1):
        if k == 0:
            break
        if s[i] == '0' and s[i+1] == '1':
            s[i] = '1'
            k -= 1

    print(s.count('1'))