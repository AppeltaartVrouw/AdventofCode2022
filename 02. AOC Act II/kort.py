def code():
    eind_res = {'A X': 3 + 1,
                'B Y': 3 + 2,
                'C Z': 3 + 3,
                'A Y': 6 + 2,
                'B Z': 6 + 3,
                'C X': 6 + 1,
                'A Z': 0 + 3,
                'B X': 0 + 1,
                'C Y': 0 + 2}
    return sum(eind_res[x] for x in open('input.txt', 'r')
               .read().rstrip('\n').split('\n'))


if __name__ == '__main__':
    print(code())
