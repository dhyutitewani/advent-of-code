import re

def calculate(num1, num2, direction):
    if direction == "L":
        return (num1 - num2) % 100
    return (num1 + num2) % 100 

def parse_input(file_path):
    num = 50
    zeros = 0
    with open(file_path, 'r') as f:
        for line in f:
            direction, n = re.match(r"([LR])(\d+)", line.strip()).groups()
            num = calculate(num, int(n), direction)
            zeros += num == 0
    return zeros

if __name__ == '__main__':
    print(parse_input('input_data/1.txt'))
