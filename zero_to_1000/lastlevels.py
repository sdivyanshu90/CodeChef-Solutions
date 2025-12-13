# cook your dish here
for _ in range(int(input())):
    level, minutes, breaks = map(int, input().split())
    if level <= 3:
        print(level * minutes)
    else:
        if level % 3 == 0:
            no_of_breaks = level // 3
            part1 = (no_of_breaks - 1) * breaks
            part2 = 3 * no_of_breaks * minutes
            tot = part1 + part2
            print(tot)
            # print(f"No. of Breaks: {no_of_breaks}\nRemaining Levels: {rem}")
            # print(f"Tot\nPart 1: {part1}\nPart 2: {part2}\nPart 3: {part3}")
        else:
            no_of_breaks = level // 3
            rem = level % 3
            part1 = no_of_breaks * breaks
            part2 = 3 * no_of_breaks * minutes
            part3 = rem * minutes
            tot = part1 + part2 + part3
            # print("-------------------")
            print(tot)
            # print(f"No. of Breaks: {no_of_breaks}\nRemaining Levels: {rem}")
            # print(f"Tot\nPart 1: {part1}\nPart 2: {part2}\nPart 3: {part3}")