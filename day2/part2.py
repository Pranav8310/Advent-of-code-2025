def part2():
    total=0
    with open('/Users/A200315862/Downloads/aoc/data/day2.txt','r') as file:
        ranges = [list(map(int, i.split('-'))) for i in file.readline().strip().split(',')]
        for i in ranges:
            for j in range(i[0], i[1] + 1):
                mid = len(str(j)) // 2
                thrice = len(str(j)) // 3
                fifth = len(str(j)) // 5
                seventh = len(str(j)) // 7
                if str(j)[:mid] == str(j)[mid:]:
                    total += j 
                elif str(j)[:thrice] == str(j)[thrice : thrice + thrice] == str(j)[thrice + thrice : ]:
                    total += j
                elif str(j)[:fifth] == str(j)[fifth : fifth + fifth] == str(j)[fifth + fifth : fifth + fifth + fifth] == str(j)[fifth + fifth + fifth : fifth + fifth + fifth + fifth] == str(j)[fifth + fifth + fifth + fifth :]:
                    total += j
                elif str(j)[:seventh] == str(j)[seventh : seventh + seventh] == str(j)[seventh + seventh : seventh + seventh + seventh] == str(j)[seventh + seventh + seventh : seventh + seventh + seventh + seventh] == str(j)[seventh + seventh + seventh + seventh : seventh + seventh + seventh + seventh + seventh] == str(j)[seventh + seventh + seventh + seventh + seventh : seventh + seventh + seventh + seventh + seventh + seventh] == str(j)[seventh + seventh + seventh + seventh + seventh + seventh:]:
                    total += j
        print(total)
if __name__=="__main__":
    print(part2())
