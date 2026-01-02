def part2():
    total = 0
    with open('aoc/data/day3.txt','r') as file:
        for f in file:
            jolts = 0
            values = list(map(int, f.strip()))
            for index in range(11):
                tens = max(values[:index - 11])
                values = values[values.index(tens) + 1:]
                jolts = (jolts * 10) + tens
            jolts = (jolts * 10) + max(values) 
            total += jolts    
        print(total)
            

if __name__=="__main__":

    part2()
