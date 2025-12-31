def part1():
    total = 0
    with open('/aoc/data/day3.txt','r') as fi:
        for file in fi:
            file = list(map(int, file.strip()))
            tens = max(file[:-1])
            first = max(file[file.index(tens) + 1:])
            total += tens * 10 + first
        print(total)


if __name__ == '__main__':
    part1() 

