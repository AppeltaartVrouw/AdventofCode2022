def code():
    with open('input.txt', 'r') as bestand:
        seq = bestand.read().rstrip()
    for i in range(len(seq)):
        if len(set(seq[i:i+4])) == 4:
            antwoord = i + 4
            break
    return antwoord


if __name__ == '__main__':
    print(code())
