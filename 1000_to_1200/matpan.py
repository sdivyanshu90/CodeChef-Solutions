# cook your dish here
from string import ascii_lowercase

alphabet = ascii_lowercase

for _ in range(int(input())):
    num = list(map(int, input().split()))
    n = input()
    res = 0
    for i in range(len(alphabet)):
        if alphabet[i] not in n:
            res += num[i]
    print(res)