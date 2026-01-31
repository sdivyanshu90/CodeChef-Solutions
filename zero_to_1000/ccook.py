# Question Link: https://www.codechef.com/problems/CCOOK

# cook your dish here
for i in range(int(input())):
    p = list(map(int, input().split()))
    s = {
        0: "Beginner",
        1: "Junior Developer",
        2: "Middle Developer",
        3: "Senior Developer",
        4: "Hacker",
        5: "Jeff Dean"
    }
    add = sum(p)
    print(s[add])