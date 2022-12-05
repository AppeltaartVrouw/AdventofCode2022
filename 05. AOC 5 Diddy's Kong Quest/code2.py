def parsen():
    with open('input.txt', 'r') as bestand:
        inhoud = bestand.read()
    kratten = {}
    kratten_index, bew_instr = inhoud.split('\n\n')
    kol_num = int(kratten_index.split('\n')[-1][-1])
    for i in range(1, kol_num+1):
        kratten[i] = []
    for rij in kratten_index.split('\n')[::-1][1:]:
        for kolom, krat in enumerate(range(-1, len(rij)+1, 4)):
            if krat < 0:
                continue
            letter = rij[krat-3:krat][1]
            if letter != ' ':
                kratten[kolom].append(rij[krat-3:krat][1])
    return kratten, bew_instr.rstrip()


def code():
    kratten, bew_instr = parsen()
    for instructie in bew_instr.split('\n'):
        inst = instructie.split()
        verp = kratten[int(inst[3])][-int(inst[1]):]
        del kratten[int(inst[3])][-int(inst[1]):]
        kratten[int(inst[5])].extend(verp)
    return "".join(kratten[x][-1] for x in kratten.keys())


if __name__ == '__main__':
    print(code())
