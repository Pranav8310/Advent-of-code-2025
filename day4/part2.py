def part2():
    count = 0
    matrix = [list(lines.strip()) for lines in open("/Users/A200315862/Downloads/aoc/aoc2025/data/day4.txt",'r')]
    while True:
        copy = [row[:] for row in matrix]
        iteration_count = 0
        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                if col=='@':
                    region = [subarray[max(0,c-1):c+2] for subarray in matrix[max(0,r-1):r+2]]
                    if sum(row.count("@") for row in region)<=4:
                        iteration_count += 1
                        copy[r][c]='.'
        if iteration_count == 0: break
        count += iteration_count
        matrix = copy
    print(count)


if __name__== "__main__":
    part2()

