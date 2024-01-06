import re 

def sum_calc(vs):
    l = []
    cs = set()

    for r, row in enumerate(vs):
        for c, char in enumerate(row):
            if char.isdigit() or char == '.':
                continue
            for sr in range(r-1,r+2):
                for sc in range(c-1,c+2):
                    if sr < 0 or sr >= len(vs) or sc < 0 or sc >= len(vs[sr]) or not vs[sr][sc].isdigit():
                        continue
                    while sc > 0 and vs[sr][sc-1].isdigit():
                        sc -= 1
                    cs.add((sr, sc))

    for a, b in cs:
        n = ''
        while b < len(vs[a]) and vs[a][b].isdigit():
            n += vs[a][b]
            b += 1
        l.append(int(n))

    print(sum(l))

def main():
    with open(r'input_data/1.txt','r') as f:
        ls = f.read().splitlines()

    sum_calc(ls)

if __name__ == '__main__':
    main()
    