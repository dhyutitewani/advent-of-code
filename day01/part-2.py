import re


def calculate(num1, num2, direction):
    zeros = 0
    result = 0
    if direction == "L":
        result = (num1 - num2) % 100
        zeros = ((100 - num1) % 100 + num2) // 100
    else:
        result = (num1 + num2) % 100
         
    
    return result, zeros


def parse_input(file_path):
    num = 50
    zeroc = 0
    with open(file_path, 'r') as f:
        for line in f:
            direction, n = re.match(r"([LR])(\d+)", line.strip()).groups()
            num, z = calculate(num, int(n), direction)
            zeroc += z
            
    return zeroc

if __name__ == '__main__':
    print(parse_input('input_data/1.txt'))
