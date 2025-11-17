# Question Link: https://www.codechef.com/problems/SPECIALITY

# cook your dish here
for _ in range(int(input())):
    setter, tester, editorialist = map(int, input().split())
    if setter > tester and setter > editorialist:
        print("Setter")
    elif tester > setter and tester > editorialist:
        print("Tester")
    else:
        print("Editorialist")