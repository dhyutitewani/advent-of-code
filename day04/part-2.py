import re

with open("input_data/1.txt") as f:
    data = f.read().splitlines()

s = 0
d = {key: 1 for key in range(1, len(data) + 1)}

for idx, ln in enumerate(data):
    cld = ln.split(":", 1)[1].strip()
    vs_r = cld.split("|", 1)[0].strip()
    vs_l = cld.split("|", 1)[1].strip()

    v_r = re.findall(r"(?:\d+)", vs_r)
    v_l = re.findall(r"(?:\d+)", vs_l)

    c = 0
    for v in v_r:
        for v_2 in v_l:
            if v == v_2:
                c += 1

    card_no = idx + 1
    for _ in range(d[card_no]):
        for j in range(card_no + 1,  card_no + c + 1):
            d[j] += 1

s = sum(d.values())
print(s)

