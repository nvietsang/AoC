def process(s):
    s = s.replace("zero", "z0o")
    s = s.replace("one", "o1e")
    s = s.replace("two", "t2o")
    s = s.replace("three", "t3e")
    s = s.replace("four", "f4r")
    s = s.replace("five", "f5e")
    s = s.replace("six", "s6x")
    s = s.replace("seven", "s7e")
    s = s.replace("eight", "e8t")
    s = s.replace("nine", "n9e")
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
    assert process("two1nine") == 29
    assert process("eightwothree") == 83
    assert process("abcone2threexyz") == 13
    assert process("xtwone3four") == 24
    assert process("4nineeightseven2") == 42
    assert process("zoneight234") == 14
    assert process("7pqrstsixteen") == 76



# test()
f = open("../infiles/input-01b.txt", "r")
data = f.readlines()
f.close()

sum = 0
for line in data:
    line = line.strip()
    n = process(line)
    sum += n

print(sum)