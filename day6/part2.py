def foo():
    a = [file.strip("\n") for file in open("/aoc/aoc2025/data/day6.txt",'r')]
    cols = list(zip(*a))
    groups = []
    group = []
    for col in cols:
        if set(col) == {" "}:
            groups.append(group)
            group = []
        else:
            group.append(col)
    groups.append(group)
    total = 0
    for group in groups:
        total += eval(group[0][-1].join("".join(line[:-1]) for line in group))
    print(total)


if __name__=="__main__":
    foo()
