import re

with open('input_data/1.txt') as f:
    data = f.readlines()

v_b = [list(map(int, re.findall(r'\d+ (?=blue)', ln))) for ln in data]
v_g = [list(map(int, re.findall(r'\d+ (?=green)', ln))) for ln in data]
v_r = [list(map(int, re.findall(r'\d+ (?=red)', ln))) for ln in data]

s = 0
for i, _ in enumerate(v_b):
    t_b = t_g = t_r = 0

    t_b = max(v_b[i])
    t_g = max(v_g[i])
    t_r = max(v_r[i])

    if t_b <= 14 and t_g <= 13 and t_r <= 12:
        s += (i+1)

print(s)
