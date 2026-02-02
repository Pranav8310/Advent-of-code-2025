def foo():
    ranges_txt, numbers_txt = open('/aoc/aoc2025/data/day5.txt').read().split('\n\n')

    ranges = [tuple(map(int, r.split("-"))) for r in ranges_txt.splitlines()]
    print(ranges)
    numbers = set(map(int, numbers_txt.splitlines())) 
    print(numbers)

    counted = set()

    for n in numbers:
        for start, end in ranges:
            if start <= n <= end:
                counted.add(n)
                break 

    print(len(counted))


if __name__ == "__main__":
    foo()
