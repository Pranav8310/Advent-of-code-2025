def bar():
    ranges= open('/Users/A200315862/Downloads/aoc/aoc2025/data/day5.txt').read()
    ranges = [tuple(map(int, r.split("-"))) for r in ranges.splitlines()]
    ranges.sort()
    last = None
    count = 0 
    for i, j in ranges:
        if last == None:
            last = (i, j)
        elif last[1] < i:
            #print(last[1], last[0], i)
            count += last[1] - last[0] + 1
            last = (i , j)
            #print(count, last)
        else:
            last = (last[0], max(last[1],j))
    count += last[1] - last[0] + 1
    print(count)
        

if __name__=='__main__':
    bar()
