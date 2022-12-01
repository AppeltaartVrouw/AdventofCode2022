def code():
    elven = [] # alle elven die het eten dragen
    with open('input.txt', 'r') as bestand:
        inhoud = bestand.read().rstrip().split('\n')
        calo_groep = []
        for voedsel in inhoud:
            # print(voedsel)
            if voedsel == '':
                elven.append(calo_groep)
                calo_groep = []
                continue
            calo_groep.append(int(voedsel))
    max_calo = []
    for bundel in elven:
        max_calo.append(sum(bundel))
    max_calo.sort()
    return sum(max_calo[-3:])


if __name__ == '__main__':
    print(code())
