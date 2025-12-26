def part2():
    total=0
    with open('/Users/a200315862/Downloads/aoc/data/day2.txt','r') as file:
        ranges = [list(map(int, i.split('-'))) for i in file.readline().strip().split(',')]
        for i in ranges:
            for j in range(i[0], i[1] + 1):
                mid = len(str(j)) // 2
                mango = len(str(j)) // 3
                peru = len(str(j)) // 5
                pen = len(str(j)) // 7
                if str(j)[:mid] == str(j)[mid:]:
                    total += j 
                elif str(j)[:mango] == str(j)[mango : mango + mango] == str(j)[mango + mango : ]:
                    total += j
                elif str(j)[:peru] == str(j)[peru : peru + peru] == str(j)[peru + peru : peru + peru + peru] == str(j)[peru + peru + peru : peru + peru + peru + peru] == str(j)[peru + peru + peru + peru :]:
                    total += j
                elif str(j)[:pen] == str(j)[pen : pen + pen] == str(j)[pen + pen : pen + pen + pen] == str(j)[pen + pen + pen : pen + pen + pen + pen] == str(j)[pen + pen + pen + pen : pen + pen + pen + pen + pen] == str(j)[pen + pen + pen + pen + pen : pen + pen + pen + pen + pen + pen] == str(j)[pen + pen + pen + pen + pen + pen:]:
                    total += j
        print(total)
if __name__=="__main__":
    print(part2())
