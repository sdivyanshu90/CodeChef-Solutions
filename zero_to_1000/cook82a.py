# cook your dish here
for _ in range(int(input())):
    scores = dict(input().split() for _ in range(4))

    winner = (
        "Barcelona"
        if scores["Barcelona"] > scores["Eibar"]
        and scores["RealMadrid"] < scores["Malaga"]
        else "RealMadrid"
    )
    print(winner)