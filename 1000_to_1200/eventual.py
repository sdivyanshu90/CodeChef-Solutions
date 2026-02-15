# Question Link: https://www.codechef.com/problems/EVENTUAL

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
            
    # for char, frequency in freq.items():
    #     print(f"Character: {char}, Frequency: {frequency}")
    # print("--------------------END------------------------")
    flag = True
    for key, val in freq.items():
        if val % 2 != 0:
            flag = False
            break
            
    if flag:
        print("YES")
    else:
        print("NO")
            