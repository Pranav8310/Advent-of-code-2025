def part2():
    start = 50
    password = 0
    with open('/aoc/data/day1.txt','r') as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            value = int(line[1:])
            for _ in range(value):
                if direction == 'L':
                    start = (start - 1) % 100
                elif direction == 'R':
                    start = (start + 1) % 100
                if start == 0:
                    password += 1

        return password
if __name__ == "__main__":
    print(part2())

