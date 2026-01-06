def foo():
    count = 0
    files = [list(line.strip()) for line in open('/aoc/aoc2025/data/day4.txt', 'r')]
    for c, col in enumerate(files):
        for r, row in enumerate(col):
            if row == '@':
                region = [subarray[max(0, r - 1): r + 2] for subarray in files[max(0, c - 1): c + 2]]
                if sum(col.count("@") for col in region) <= 4:
                    count += 1
    print(count)                    

if __name__ == '__main__':
    foo()
