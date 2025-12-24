def secret():

    start = 50
    password = 0
    file_path = "/aoc/data/day1.txt" 

    with open(file_path, 'r') as file:
        for lines in file:
            lines = lines.strip()
            direction = lines[0]
            value = int(lines[1:])

            if direction == 'L':
                start = (start - value)%100
            elif direction == 'R':
                start = (start + value)%100

            if start == 0:
                password += 1
        return password 

if __name__ == "__main__":
    print(secret())
