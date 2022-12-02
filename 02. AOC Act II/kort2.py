def code():
    eind_res = {'A X': 0 + 3,
                'C X': 0 + 2,
                'B X': 0 + 1,
                'B Y': 3 + 2,
                'A Y': 3 + 1,
                'C Y': 3 + 3,
                'C Z': 6 + 1,
                'B Z': 6 + 3,
                'A Z': 6 + 2}
    return sum(eind_res[x] for x in open('input.txt', 'r')
               .read().rstrip('\n').split('\n'))


if __name__ == '__main__':
    print(code())
