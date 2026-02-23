# Question: https://www.codechef.com/problems/HOLES

# cook your dish here
for _ in range(int(input())):
    s = input()
    res = 0
    for char in s:
        if char in ["A", "D", "O", "P", "Q", "R"]:
            res += 1
        elif char == "B":
            res += 2
    print(res)