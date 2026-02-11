def foo():
    a = [f.split() for f in open("/Users/A200315862/Downloads/aoc/aoc2025/data/day6.txt",'r')]
    total = 0
    for *i,col in zip(*a):
        sum = eval(col.join(i))
        total += sum 
    print(total)
            
if __name__=="__main__":
    foo()
