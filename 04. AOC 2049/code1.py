def code():
    with open('input.txt', 'r') as bestand:
        inhoud = bestand.read().rstrip().split('\n')
    tal = 0
    for idn in inhoud:
        r1, r2 = idn.split(',')
        r1, r2 = r1.split('-'), r2.split('-')
        if (int(r1[0]) in range(int(r2[0]), int(r2[1])+1) and
                int(r1[1]) in range(int(r2[0]), int(r2[1])+1)) or \
            (int(r2[0]) in range(int(r1[0]), int(r1[1])+1) and
             int(r2[1]) in range(int(r1[0]), int(r1[1])+1)):
            tal += 1
    return tal


if __name__ == '__main__':
    print(code())
