# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = map(int, input().split())

    count_res0 = count_res1 = count_res2 = 0

    for x in A:
        r = x % 3
        if r == 0:
            print("Yes")
            break
        elif r == 1:
            count_res1 += 1
        else:
            count_res2 += 1

        if (count_res1 > 0 and count_res2 > 0) or count_res1 >= 3 or count_res2 >= 3:
            print("Yes")
            break
    else:
        print("No")