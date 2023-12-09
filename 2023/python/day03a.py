import string
import re

SYMBOLS = set(string.punctuation) - set(".")
MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def process(data):
    Nr = len(data)
    Nc = len(data[0])

    sum = 0

    for l, line in enumerate(data):
        pos = re.finditer(r'\d+', line)
        for p in pos:
            L = p.start()
            R = p.end()
            is_adjacent = False
            for c in range(L-1, R+1):
                r = l - 1
                if 0 <= r < Nr and 0 <= c < Nc and data[r][c] in SYMBOLS:
                    is_adjacent = True
                    break
                r = l + 1
                if 0 <= r < Nr and 0 <= c < Nc and data[r][c] in SYMBOLS:
                    is_adjacent = True
                    break
            
            r = l
            c = L - 1
            if 0 <= r < Nr and 0 <= c < Nc and data[r][c] in SYMBOLS:
                is_adjacent = True
            
            r = l
            c = R
            if 0 <= r < Nr and 0 <= c < Nc and data[r][c] in SYMBOLS:
                is_adjacent = True            

            # print(p.group(), is_adjacent)
            if is_adjacent:
                sum += int(p.group())
    return sum


def test():
    data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.splitlines()
    print(data)

    sum = process(data)
    print(sum)

# test()

f = open("../infiles/input-03.txt", "r")
data = f.readlines()
data = [line.strip() for line in data]

sum = process(data)
print(sum)