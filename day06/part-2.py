import re

with open('input_data/2.txt') as f:
    data = f.readlines()

vs = [list(map(int, re.findall(r'\d+', ln))) for ln in data]

r = 0
for j in range(1, vs[0][0]):
    dist = j * (vs[0][0] - j)
    if (dist > vs[1][0]): r += 1

print(r)
