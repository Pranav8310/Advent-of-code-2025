def part():
    with open('/Users/a200315862/Downloads/aoc/data/day2.txt','r') as file:

        ranges = [list(map(int, i.split("-"))) for i in file.readline().strip().split(",")]
        #print(ranges)
        total = 0
        for i in ranges:
            #print(i)
            for j in range(i[0], i[1] + 1):
                mid = len(str(j)) // 2
                if str(j)[:mid] == str(j)[mid:]:
                    total += j
        print(total)


if __name__=='__main__':
    print(part())
