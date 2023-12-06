from word2number import w2n

d = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def sum_nums(ln):
    l=[]

    for i, _ in enumerate(ln):
        for j in range(i, len(ln)+1):
            if ln[i:j] in d:
                num = w2n.word_to_num(ln[i:j])
                l.append(str(num))
        if ln[i].isdigit():
            l.append(ln[i])

    num = int(l[0] + l[-1])
    return num

def main():
    with open('input_data/2.txt','r') as f:
        ls = f.readlines()

    s = 0
    for ln in ls:
        s += sum_nums(ln)

    print(s)

if __name__ == '__main__':
    main()