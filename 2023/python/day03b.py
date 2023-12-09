import re
import string
from collections import defaultdict

SYMBOLS = set(string.punctuation) - set(".")

# f = open("../infiles/test-03.txt")
f = open("../infiles/input-03.txt")
data = f.readlines()
f.close()

data = [line.strip() for line in data]
Nr = len(data)
Nc = len(data[0])

star_indices = defaultdict(list)

for l, line in enumerate(data):
    nums = re.finditer(r'\d+', line)
    for num in nums:
        L = num.start()
        R = num.end()

        for c in range(L-1, R+1):
            r = l - 1
            if 0 <= r < Nr and 0 <= c < Nc and data[r][c] == "*":
                star_indices[(r, c)].append(num.group())
            r = l + 1
            if 0 <= r < Nr and 0 <= c < Nc and data[r][c] == "*":
                star_indices[(r, c)].append(num.group())
            
        r = l
        c = L - 1
        if 0 <= r < Nr and 0 <= c < Nc and data[r][c] == "*":
            star_indices[(r, c)].append(num.group())
        r = l
        c = R
        if 0 <= r < Nr and 0 <= c < Nc and data[r][c] == "*":
            star_indices[(r, c)].append(num.group())

s = sum([int(v[0]) * int(v[1]) for v in star_indices.values() if len(v) == 2])
print(s)