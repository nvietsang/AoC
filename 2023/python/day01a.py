
def process(s):
    
    for c in s:
        if c.isnumeric():
            n1 = int(c)
            break
    for c in reversed(s):
        if c.isnumeric():
            n2 = int(c)
            break
    n = n1 * 10 + n2    
    return n

def test():
    assert process("1abc2") == 12
    assert process("pqr3stu8vwx") == 38
    assert process("a1b2c3d4e5f") == 15
    assert process("treb7uchet") == 77

# test()
f = open("../infiles/input-01a.txt", "r")
data = f.readlines()
f.close()

sum = 0
for line in data:
    line = line.strip()
    n = process(line)
    sum += n

print(sum)