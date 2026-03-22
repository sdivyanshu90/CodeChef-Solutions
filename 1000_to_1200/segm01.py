# Question Link: https://www.codechef.com/problems/SEGM01

# cook your dish here
for _ in range(int(input())):
    s = input()
    if '1' not in s:
        print('NO')
    else:
        start = s.index('1')
        end = s.rindex('1')
        if '0' in s[start:end+1]:
            print('NO')
        else:
            print('YES')