def code():
    with open('input.txt', 'r') as bestand:
        inhoud = bestand.read().rstrip().split('\n')
    tal = 0
    for idn in inhoud:
        r1, r2 = idn.split(',')
        r1, r2 = r1.split('-'), r2.split('-')
        s1 = set(range(int(r1[0]), int(r1[1])+1))
        s2 = set(range(int(r2[0]), int(r2[1]) + 1))
        overlap = s1 & s2
        if len(overlap) > 0:
            tal += 1
    return tal


if __name__ == '__main__':
    print(code())
